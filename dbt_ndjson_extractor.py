import json
import os
from pathlib import Path
from typing import Union

import agate


class NDJSONExtractor:
    def __init__(self, model):
        self.model = model

    def extract(self):
        potential_paths: list[Path] = [
            (Path(self.model.root_path) / Path(self.model.path)).parent
            / self.model.config._extra.get("filename", "<custom filename>"),
            (Path(self.model.root_path) / Path(self.model.path)).parent
            / f"{self.model.name}.ndjson",
            (Path(self.model.root_path) / Path(self.model.path)).parent
            / f"{self.model.name}.jsonl",
        ]

        path = None

        for p in potential_paths:
            if p.is_file():
                path = p
                break

        if path is None:
            raise RuntimeError(
                f"Could not find ndjson file at any of the following paths: {potential_paths}"
            )

        return agate.Table.from_json(path, newline=True)
