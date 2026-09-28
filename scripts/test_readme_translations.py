#!/usr/bin/env python3
"""Regression tests for README translation freshness and structure checks."""

from __future__ import annotations

import hashlib
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_readme_translations as translations


def nav(locale: str | None) -> str:
    if locale is None:
        links = [(info["flag"], info["path"]) for info in translations.LANGUAGES.values()]
    else:
        links = [(translations.ENGLISH, "../README.md")]
        links.extend((info["flag"], Path(info["path"]).name) for info in translations.LANGUAGES.values())
    rendered = " · ".join(f"[{flag}]({target})" for flag, target in links)
    return f"{translations.NAV_START}\n{rendered}\n{translations.NAV_END}"


def source_readme() -> str:
    return f"""# Moon Source

{nav(None)}

## Purpose

[Architecture](ARCHITECTURE.md)

| Need | Route |
|---|---|
| One | [Start](START_HERE.md) |

- One useful action.

> One bounded quote.

Use \x60MOON_SOURCE_AI_KERNEL.md\x60 for routing.

~~~text
Describe the task.
~~~

\x60\x60\x60bash
python scripts/moon_source.py validate
\x60\x60\x60

\x60\x60\x60mermaid
flowchart TB
    first["First"]
    second["Second"]
    first --- second
\x60\x60\x60

<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->
- A registered item.
<!-- MOON-SOURCE-CAPABILITY-DIGEST:END -->

<!-- MOON-SOURCE-PUBLIC-STAMP -->
"""


def translated_readme(locale: str, sha: str) -> str:
    info = translations.LANGUAGES[locale]
    return f"""# Moon Source

<!--
MOON-SOURCE-README-TRANSLATION
locale: {locale}
source: ../README.md
source_sha256: {sha}
contract: ../docs/README_TRANSLATIONS.md
-->

{nav(locale)}

{info["authority"]}. Moon Source remains the semantic authority.

## Purpose

[Arquitetura](../ARCHITECTURE.md)

| Necesidad | Ruta |
|---|---|
| Uno | [Inicio](../START_HERE.md) |

- Una acción útil.

> Una cita delimitada.

Usa \x60MOON_SOURCE_AI_KERNEL.md\x60 para el enrutamiento.

~~~text
Describe la tarea.
~~~

\x60\x60\x60bash
python scripts/moon_source.py validate
\x60\x60\x60

\x60\x60\x60mermaid
flowchart TB
    first["Primero"]
    second["Segundo"]
    first --- second
\x60\x60\x60

<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->
- Un elemento registrado.
<!-- MOON-SOURCE-CAPABILITY-DIGEST:END -->

<!-- MOON-SOURCE-PUBLIC-STAMP -->
"""


def fixture() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    temporary = tempfile.TemporaryDirectory()
    root = Path(temporary.name)
    (root / "translations").mkdir()
    (root / "docs").mkdir()
    (root / "docs" / "README_TRANSLATIONS.md").write_text("Translation contract fixture\n", encoding="utf-8")
    source = source_readme()
    (root / "README.md").write_text(source, encoding="utf-8")
    sha = hashlib.sha256(source.encode("utf-8")).hexdigest()
    for locale, info in translations.LANGUAGES.items():
        (root / info["path"]).write_text(translated_readme(locale, sha), encoding="utf-8")
    return temporary, root


def main() -> None:
    temporary, root = fixture()
    try:
        assert translations.validate(root) == [], translations.validate(root)
    finally:
        temporary.cleanup()

    for locale, info in translations.LANGUAGES.items():
        temporary, root = fixture()
        try:
            (root / info["path"]).unlink()
            failures = translations.validate(root)
            assert any(info["path"] in failure for failure in failures), failures
        finally:
            temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["es"]["path"]
        current = path.read_text(encoding="utf-8")
        metadata = translations.METADATA_RE.search(current)
        assert metadata
        path.write_text(current.replace(metadata.group("sha"), "0" * 64, 1), encoding="utf-8")
        assert any("source_sha256 is stale" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["es"]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("locale: es", "locale: ru"), encoding="utf-8")
        assert any("metadata locale" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["zh-CN"]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("[🇪🇸](README.es.md)", "[🇪🇸](missing.md)"), encoding="utf-8")
        assert any("language-navigation routes" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["ru"]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->", ""), encoding="utf-8")
        assert any("automation marker" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["pt-BR"]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("../ARCHITECTURE.md", "../MISSING.md"), encoding="utf-8")
        assert any("Markdown targets differ" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    temporary, root = fixture()
    try:
        path = root / translations.LANGUAGES["pt-BR"]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace(
            "python scripts/moon_source.py validate", "python scripts/moon_source.py changed"
        ), encoding="utf-8")
        assert any("shell command block" in failure for failure in translations.validate(root))
    finally:
        temporary.cleanup()

    required = {info["path"] for info in translations.LANGUAGES.values()}
    failures = translations.cochange_failures({"README.md", "translations/README.pt-BR.md"})
    assert failures and all(path in failures[0] for path in required - {"translations/README.pt-BR.md"})
    assert translations.cochange_failures({"README.md", *required}) == []
    assert translations.cochange_failures({"docs/TERMINOLOGY.md"}) == []

    temporary, root = fixture()
    try:
        with patch.dict(os.environ, {}, clear=True):
            assert translations.pull_request_changed_paths(root) is None
            assert translations.validate(root) == []
    finally:
        temporary.cleanup()

    print("README translation regression tests passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
