from pathlib import Path

class TextFile:
    def __init__(self, file_path: str):
        self.path = Path(file_path)

    def read(self) -> str:
        if not self.path.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {self.path}")
        return self.path.read_text(encoding="utf-8")

    def write(self, content: str):
        self.path.write_text(content, encoding="utf-8")

