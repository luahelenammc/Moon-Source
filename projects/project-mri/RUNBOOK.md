# Project MRI runbook

## Clean run

From the repository root:

```bash
python -m unittest discover -s tests -v
python -m mri demo --output out/demo
python -m mri eval fixtures/northstar --output evals/northstar
```

Expected demo summary: 9 documents, 10 extracted objects, 15 findings and a changed before/after proxy. Expected Northstar result: 8/8 recovered.

## Start the web demo

```bash
python server.py
```

Open `http://127.0.0.1:8000`. The server uses only the checked-in synthetic corpus. `GET /api/health` confirms the version; `GET /api/scan` produces the current result; `POST /api/reset` resets the review state.

## Review recovery

If a review state is not useful for the walkthrough, click **Reset review state** or run:

```bash
curl -X POST http://127.0.0.1:8000/api/reset
```

Approval is recorded in memory only and never changes the fixture.

## Failure recovery

- **No supported documents:** provide a folder or ZIP containing UTF-8 `.md`, `.markdown` or `.txt` files.
- **Unsafe ZIP member:** remove absolute paths, `..` traversal and symlink members.
- **Symlink error:** copy the corpus into a real directory tree before scanning.
- **Port occupied:** use `MRI_PORT=8765 python server.py`.
- **Report before scan:** the report route creates the deterministic scan automatically.
- **Provider status:** `python -m mri nutrient-status` reports the optional adapter state; disabled is the expected public-build state.

## Public demo rule

Use synthetic fixtures only. Do not point the demo at hospital, patient, collaborator, private source or connector data, and do not add credentials to the environment or screenshots.
