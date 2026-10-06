#!/usr/bin/env python3
"""Repository-level check of the telemetry contract. Does not verify runtime behavior."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def validate(doc, schema, catalog):
    errs = [f"missing: {k}" for k in schema["required"] if k not in doc]
    errs += [f"unexpected: {k}" for k in doc if k not in schema["properties"]]
    if doc.get("schema_version") != "1":
        errs.append("bad schema_version")
    if "event_name" in doc and doc["event_name"] not in catalog["events"]:
        errs.append("unknown event_name")
    if "payload" in doc and not isinstance(doc["payload"], dict):
        errs.append("payload not object")
    return errs


def main():
    schema = json.loads((ROOT / "schemas/telemetry-envelope.schema.json").read_text())
    catalog = json.loads((ROOT / "schemas/event-catalog.v1.json").read_text())
    failed = False
    for kind, expect_ok in (("valid", True), ("invalid", False)):
        for f in sorted((ROOT / "fixtures" / kind).glob("*.json")):
            ok = not validate(json.loads(f.read_text()), schema, catalog)
            if ok != expect_ok:
                print(f"FAIL {f.relative_to(ROOT)}")
                failed = True
    print("REPOSITORY_CHECKED" if not failed else "FAILED", "(runtime: NOT_VERIFIED)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
