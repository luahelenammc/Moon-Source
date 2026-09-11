from pathlib import Path
import json


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing anchor: {label}")
    return text.replace(old, new, 1)


registry_path = Path("registry/public-capabilities.json")
data = json.loads(registry_path.read_text(encoding="utf-8"))
chat = next(c for c in data["capabilities"] if c["id"] == "chat-work-routing")
dist = chat["distribution"]
dist["composite"] = True
dist["composite_members"] = [
    {
        "archive_path": "CHAT_WORK_ROUTING_PROTOCOL_V4.md",
        "source_path": "portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md",
    },
    {
        "archive_path": "astra/CHAT_WORK_ASTRA_ADAPTER.md",
        "source_path": "portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md",
    },
]
registry_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

validator_path = Path("scripts/validate_public_capabilities.py")
validator = validator_path.read_text(encoding="utf-8")
old = '''                    if distribution.get("composite"):
                        if path.name not in {Path(name).name for name in files}:
                            errors.append(f"{capability_id} composite package omits its canonical body")
                    else:
'''
new = '''                    if distribution.get("composite"):
                        members = distribution.get("composite_members")
                        if members is not None:
                            if not isinstance(members, list) or not members or not all(isinstance(member, dict) for member in members):
                                errors.append(f"{capability_id} composite_members must be a non-empty array of objects")
                            else:
                                expected_names = [member.get("archive_path") for member in members]
                                source_paths = [member.get("source_path") for member in members]
                                if any(not isinstance(name, str) or not name for name in expected_names):
                                    errors.append(f"{capability_id} composite package has invalid archive_path")
                                elif any(not isinstance(source, str) or not source for source in source_paths):
                                    errors.append(f"{capability_id} composite package has invalid source_path")
                                elif len(set(expected_names)) != len(expected_names):
                                    errors.append(f"{capability_id} composite package has duplicate archive_path")
                                elif files != expected_names:
                                    errors.append(f"{capability_id} composite package members do not match contract")
                                else:
                                    if canonical_path not in source_paths:
                                        errors.append(f"{capability_id} composite package contract omits canonical source")
                                    for member in members:
                                        source = root / member["source_path"]
                                        if not source.is_file():
                                            errors.append(
                                                f"{capability_id} composite package source is missing: {member['source_path']}"
                                            )
                                        elif archive.read(member["archive_path"]) != source.read_bytes():
                                            errors.append(
                                                f"{capability_id} composite package member mismatch: {member['archive_path']}"
                                            )
                        elif path.name not in {Path(name).name for name in files}:
                            errors.append(f"{capability_id} composite package omits its canonical body")
                    else:
'''
validator = replace_once(validator, old, new, "composite validator branch")
validator_path.write_text(validator, encoding="utf-8")

test_path = Path("scripts/test_validate_public_capabilities.py")
tests = test_path.read_text(encoding="utf-8")
insert_after = '''    def test_package_must_contain_exact_canonical_bytes(self):
        data = copy.deepcopy(self.data)
        self._write_package("CONNECTED_SOURCES.md", "different bytes")
        self.assert_error("exactly the canonical bytes", self.errors(data))

'''
new_test = '''    def test_composite_package_members_are_byte_verified(self):
        data = copy.deepcopy(self.data)
        capability = data["capabilities"][0]
        adapter_path = self.root / "docs/ADAPTER.md"
        adapter_path.write_text("adapter bytes", encoding="utf-8")
        capability["distribution"]["composite"] = True
        capability["distribution"]["composite_members"] = [
            {
                "archive_path": "CONNECTED_SOURCES.md",
                "source_path": "docs/CONNECTED_SOURCES.md",
            },
            {
                "archive_path": "adapter/ADAPTER.md",
                "source_path": "docs/ADAPTER.md",
            },
        ]
        canonical = (self.root / "docs/CONNECTED_SOURCES.md").read_bytes()
        with ZipFile(self.root / "downloads/connected-sources.zip", "w") as archive:
            archive.writestr("CONNECTED_SOURCES.md", canonical)
            archive.writestr("adapter/ADAPTER.md", b"adapter bytes")
        self.assertEqual(self.errors(data), [])

        with ZipFile(self.root / "downloads/connected-sources.zip", "w") as archive:
            archive.writestr("CONNECTED_SOURCES.md", canonical)
            archive.writestr("adapter/ADAPTER.md", b"drifted bytes")
        self.assert_error("composite package member mismatch", self.errors(data))

'''
tests = replace_once(tests, insert_after, insert_after + new_test, "composite package regression test")
test_path.write_text(tests, encoding="utf-8")
