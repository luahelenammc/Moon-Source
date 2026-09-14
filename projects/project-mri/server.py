from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from mri.pipeline import scan
from mri.review import apply_review, approve_plan, review_summary
from mri.nutrient import NutrientAdapter
from mri.report import render_markdown
from mri import __version__

ROOT = Path(__file__).resolve().parent
FIXTURE = ROOT / "fixtures" / "demo_corpus"
HTML = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
CURRENT_RESULT = None


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        global CURRENT_RESULT
        route = urlparse(self.path).path
        if route in {"/", "/index.html"}:
            self._send(HTML.encode("utf-8"), "text/html; charset=utf-8")
            return
        if route == "/api/health":
            self._send(json.dumps({"ok": True, "service": "project-mri", "version": __version__}).encode("utf-8"), "application/json; charset=utf-8")
            return
        if route == "/api/scan":
            CURRENT_RESULT = scan(FIXTURE)
            self._send(json.dumps(CURRENT_RESULT.to_dict(), ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")
            return
        if route == "/api/report.md":
            if CURRENT_RESULT is None:
                CURRENT_RESULT = scan(FIXTURE)
            self._send(render_markdown(CURRENT_RESULT).encode("utf-8"), "text/markdown; charset=utf-8")
            return
        if route == "/api/nutrient-status":
            self._send(json.dumps(NutrientAdapter().status(), ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")
            return
        self._send(b"Not found", "text/plain; charset=utf-8", 404)

    def do_POST(self) -> None:  # noqa: N802
        global CURRENT_RESULT
        route = urlparse(self.path).path
        if route in {"/api/review", "/api/approve", "/api/reset"}:
            if CURRENT_RESULT is None:
                CURRENT_RESULT = scan(FIXTURE)
        if route == "/api/review":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length < 0 or length > 8000:
                    self._send(b'{"error":"Request body exceeds 8000 bytes."}', "application/json; charset=utf-8", 413)
                    return
                payload = json.loads(self.rfile.read(length) or b"{}")
                item = apply_review(
                    CURRENT_RESULT.review_ledger,
                    str(payload.get("finding_id", "")),
                    str(payload.get("status", "")),
                    str(payload.get("note", "")),
                )
            except (ValueError, KeyError, json.JSONDecodeError) as exc:
                self._send(json.dumps({"error": str(exc)}).encode("utf-8"), "application/json; charset=utf-8", 400)
                return
            self._send(json.dumps({"review": item, "summary": review_summary(CURRENT_RESULT.review_ledger), "mutation_applied": False}).encode("utf-8"), "application/json; charset=utf-8")
            return
        if route == "/api/approve":
            changed = approve_plan(CURRENT_RESULT.review_ledger)
            self._send(
                json.dumps({"approved": True, "reviewed": changed, "summary": review_summary(CURRENT_RESULT.review_ledger), "mutation_applied": False, "message": "Sandbox approval recorded; no source files were changed."}).encode("utf-8"),
                "application/json; charset=utf-8",
            )
            return
        if route == "/api/reset":
            CURRENT_RESULT = scan(FIXTURE)
            self._send(json.dumps({"reset": True, "summary": review_summary(CURRENT_RESULT.review_ledger)}).encode("utf-8"), "application/json; charset=utf-8")
            return
        self._send(b"Not found", "text/plain; charset=utf-8", 404)

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    port = int(os.getenv("MRI_PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Project MRI demo: http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
