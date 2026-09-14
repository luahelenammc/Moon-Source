# Third-party notices and dependency audit

## Runtime

The MRI runtime uses Python’s standard library only. No third-party Python package is imported by the application or tests.

`setuptools` is declared only as a packaging/build backend in `pyproject.toml`; it is not a runtime dependency of the scanner or server.

## Optional provider boundary

`mri/nutrient.py` is retained as an optional adapter seam. It uses Python’s standard `urllib` client, contains no credential and is disabled by default. No live provider call is part of the reference build. Any future SDK or provider activation requires a new dependency, privacy review, terms review and verification record.

## Fixtures and assets

All checked-in fixtures and diagrams are original synthetic/project material created for this repository. No private source corpus, external dataset or copied third-party code is included.

## License handling

Third-party material, if added in a future change, must keep its own terms and be recorded here before publication. See [`LICENSING.md`](LICENSING.md).

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
