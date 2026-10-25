"""Data model package for wasth_schema."""

from pathlib import Path

from wasth_schema import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "wasth_schema.yaml"
