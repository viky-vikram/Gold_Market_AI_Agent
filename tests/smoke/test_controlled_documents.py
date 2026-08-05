"""Enforce that the seven controlled documents are present and unmodified.

Sprint 0 exit criteria require that "controlled documents are immutable except
through reviewed change process". This test makes that executable: an accidental
or silent edit fails CI, while a deliberate approved change shows up in review as
a visible checksum-manifest update.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

from controlled_documents import (  # noqa: E402
    CONTROLLED_DIR,
    CONTROLLED_DOCUMENTS,
    checksum,
    load_manifest,
)


def test_all_seven_controlled_documents_exist() -> None:
    missing = [name for name in CONTROLLED_DOCUMENTS if not (CONTROLLED_DIR / name).is_file()]
    assert not missing, f"Missing controlled documents: {missing}"


def test_controlled_document_count_is_exactly_seven() -> None:
    """The controlled set is deliberately limited to seven documents."""
    present = sorted(p.name for p in CONTROLLED_DIR.glob("*.md"))
    assert present == sorted(CONTROLLED_DOCUMENTS), (
        "docs/controlled/ must contain exactly the seven controlled documents. "
        f"Found: {present}"
    )


@pytest.mark.parametrize("name", CONTROLLED_DOCUMENTS)
def test_controlled_document_is_unmodified(name: str) -> None:
    manifest = load_manifest()
    assert name in manifest, f"{name} has no recorded checksum"
    assert checksum(CONTROLLED_DIR / name) == manifest[name], (
        f"{name} has changed.\n\n"
        "Controlled documents are read-only. If this change is approved, record it "
        "and regenerate the manifest:\n"
        "    uv run python scripts/controlled_documents.py --update"
    )
