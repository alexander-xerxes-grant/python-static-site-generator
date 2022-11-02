from typing import List
from pathlib import Path

class Parser:
    
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions():
            return extension
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path) as file:
            return file.read()
    