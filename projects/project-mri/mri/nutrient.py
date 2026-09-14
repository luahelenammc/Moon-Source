from __future__ import annotations

import os
import uuid
from dataclasses import dataclass
from html import escape
from urllib import error, request


class NutrientIntegrationError(RuntimeError):
    """A safe, actionable error from the optional Nutrient DWS adapter."""


@dataclass(frozen=True)
class NutrientConfig:
    endpoint: str = "https://api.nutrient.io"
    api_key: str = ""
    mode: str = "disabled"
    timeout_seconds: int = 20

    @classmethod
    def from_env(cls) -> "NutrientConfig":
        raw_timeout = os.getenv("NUTRIENT_DWS_TIMEOUT_SECONDS", "20")
        try:
            timeout = max(1, min(120, int(raw_timeout)))
        except ValueError:
            timeout = 20
        return cls(
            endpoint=os.getenv("NUTRIENT_DWS_ENDPOINT", "https://api.nutrient.io").rstrip("/"),
            api_key=os.getenv("NUTRIENT_DWS_API_KEY", ""),
            mode=os.getenv("NUTRIENT_DWS_MODE", "disabled").lower(),
            timeout_seconds=timeout,
        )


class NutrientAdapter:
    """Optional DWS boundary; MRI remains the diagnostic and authority owner.

    The adapter performs no network call unless the caller explicitly asks for a
    live conversion and provides an API key plus ``NUTRIENT_DWS_MODE=live``.
    """

    def __init__(self, config: NutrientConfig | None = None):
        self.config = config or NutrientConfig.from_env()

    def status(self) -> dict[str, object]:
        configured = bool(self.config.api_key)
        live_enabled = configured and self.config.mode == "live"
        return {
            "provider": "Nutrient DWS",
            "configured": configured,
            "live_enabled": live_enabled,
            "live_verified": False,
            "operation": "convert MRI evidence packet Markdown to PDF",
            "endpoint": self.config.endpoint,
            "reason": (
                "Set NUTRIENT_DWS_API_KEY and NUTRIENT_DWS_MODE=live after human account/terms approval."
                if not live_enabled
                else "Credentials are present; live verification is an explicit operator action."
            ),
        }

    def convert_markdown_to_pdf(self, markdown_text: str) -> bytes:
        if not self.config.api_key:
            raise NutrientIntegrationError(
                "Nutrient DWS is not configured: create/approve the account, set NUTRIENT_DWS_API_KEY, "
                "then enable NUTRIENT_DWS_MODE=live."
            )
        if self.config.mode != "live":
            raise NutrientIntegrationError(
                "Nutrient DWS is configured but live mode is disabled; set NUTRIENT_DWS_MODE=live explicitly."
            )
        boundary = "----project-mri-" + uuid.uuid4().hex
        html_document = "<!doctype html><html><body><pre>" + escape(markdown_text) + "</pre></body></html>"
        body = (
            f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="html"; filename="mri-evidence.html"\r\n'
            "Content-Type: text/html\r\n\r\n"
            f"{html_document}\r\n"
            f"--{boundary}--\r\n"
        ).encode("utf-8")
        endpoint = self.config.endpoint + "/processor/generate_pdf"
        req = request.Request(
            endpoint,
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.config.api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Accept": "application/pdf",
                "User-Agent": "project-mri/0.2.0",
            },
        )
        try:
            with request.urlopen(req, timeout=self.config.timeout_seconds) as response:
                payload = response.read()
        except (error.HTTPError, error.URLError, TimeoutError) as exc:
            raise NutrientIntegrationError(f"Nutrient DWS conversion failed: {exc}") from exc
        if not payload:
            raise NutrientIntegrationError("Nutrient DWS returned an empty document")
        return payload
