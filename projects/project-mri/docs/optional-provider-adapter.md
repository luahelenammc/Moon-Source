# Optional provider adapter

`mri/nutrient.py` is retained as a deliberately separated integration seam for a future document-operation provider. It is not required for the scanner, web demo, tests or evaluation.

The adapter:

- is disabled by default;
- contains no credential;
- fails closed without explicit live configuration;
- operates downstream from MRI’s evidence packet;
- cannot choose authority or apply source repairs.

No live provider call, output hash, GPU use or sponsor integration is claimed in the current build. Activating a provider would require human approval of account/terms, a fresh privacy/dependency review and a reproducible operation record.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
