"""Checksum helpers for the seven controlled specification documents.

The controlled documents are read-only. `tests/smoke/test_controlled_documents.py`
fails when one of them changes without the checksum manifest being regenerated
deliberately, which forces the change through review.

Regenerate the manifest only as part of an approved controlled-document change:

    uv run python scripts/controlled_documents.py --update
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTROLLED_DIR = REPO_ROOT / "docs" / "controlled"
MANIFEST_PATH = REPO_ROOT / "docs" / "controlled-checksums.json"

CONTROLLED_DOCUMENTS: tuple[str, ...] = (
    "Gold_Market_AI_Agent_PRD.md",
    "Gold_Market_AI_Agent_TRD.md",
    "Gold_Market_AI_Agent_UI_UX_Recommendations.md",
    "Gold_Market_AI_Agent_Application_Flow.md",
    "Gold_Market_AI_Agent_Backend_Database_Schema.md",
    "Gold_Market_AI_Agent_API_Event_Provider_Contracts.md",
    "Gold_Market_AI_Agent_Detailed_Implementation_Plan.md",
)


def checksum(path: Path) -> str:
    """Return the SHA-256 of a document with line endings normalised to LF.

    Normalising means the checksum is identical on Windows, macOS, and Linux
    regardless of how git checked the file out.
    """
    normalised = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(normalised).hexdigest()


def current_checksums() -> dict[str, str]:
    return {name: checksum(CONTROLLED_DIR / name) for name in CONTROLLED_DOCUMENTS}


def load_manifest() -> dict[str, str]:
    raw: dict[str, str] = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return raw


def write_manifest(checksums: dict[str, str]) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(checksums, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update",
        action="store_true",
        help="regenerate the manifest (approved controlled-document changes only)",
    )
    args = parser.parse_args()

    if args.update:
        write_manifest(current_checksums())
        print(f"Wrote {MANIFEST_PATH.relative_to(REPO_ROOT)}")
        return 0

    print(json.dumps(current_checksums(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
