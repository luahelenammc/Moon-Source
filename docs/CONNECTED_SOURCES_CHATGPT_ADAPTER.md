# Connected Sources — ChatGPT Adapter Notes

This is a subordinate, dated reference adapter for applying the stable [Connected Sources](../portables/connected-sources/CONNECTED_SOURCES.md) method to ChatGPT product surfaces. It owns volatile product facts only. It is not a second Connected Sources method, a vendor ontology, a registry identity or a source of universal connector support.

**Current-product check:** 2026-08-23. Verify again before relying on any product-specific detail.

## Official sources consulted

- [Google Drive app with sync — Self-Service Setup](https://help.openai.com/en/articles/10948259-google-drive-synced-connectors-self-service-setup/)
- [ChatGPT apps with sync](https://help.openai.com/en/articles/10847137-chatgpt-synced-connectors)
- [Google App for ChatGPT — Data Controls FAQ](https://help.openai.com/en/articles/10408842-google-app-for-chatgpt-data-controls-faq)
- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

## Google Drive reference facts

As checked on the date above, OpenAI documents that:

- apps with sync index selected knowledge sources in advance and can retrieve relevant information for ChatGPT responses;
- initial synchronization may be partial and may take time to complete, while later changes are refreshed regularly;
- synced apps are designed especially for question-and-answer and search tasks, with limits for aggregations across numerous sources or complex queries;
- existing source permissions remain relevant, and workspace settings or OAuth scopes can limit access and actions;
- Google Docs, Sheets and Slides actions are surfaced through the Google Drive app;
- viewing a source and updating a source are different capabilities: updates require the corresponding action, permission and scope;
- availability depends on plan, workspace settings, permissions and the ChatGPT surface.

Operational consequence: even a complete or actively refreshed index does not prove that the AI inspected every source relevant to the current question. Use targeted retrieval for scoped questions and an explicit inventory method for completeness claims.

## GitHub reference facts

As checked on the date above, OpenAI documents that:

- the GitHub app can expose repository code, README files and other documentation for search, analysis and citation;
- availability can vary by ChatGPT plan and product experience;
- repository access and a repository's sync selection are related but distinct;
- the standard ChatGPT GitHub app is read-oriented for repository analysis and search;
- generating, editing and pushing code directly to GitHub is routed to Codex rather than inferred from the read-oriented ChatGPT app.

Operational consequence: GitHub is a complementary executable-source substrate. It may govern code, branches, commits, tests or CI when the project declares those facets, while a living document or Drive-equivalent source may govern intent and semantic decisions. Do not collapse ChatGPT app access, Codex execution and GitHub repository authority into one capability.

## Use boundary

Load these notes only when current ChatGPT behavior materially affects the task. For generic source governance, load the Connected Sources portable directly. Product facts, plan availability, permissions, sync state and action surfaces must be capability-probed again when consequence makes them material.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
