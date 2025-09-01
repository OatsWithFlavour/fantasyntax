from pathlib import Path

def to_tex(txt_path: str) -> str:
    """Gibt den Pfad zur .tex-Datei zurück, basierend auf einem .txt-Pfad."""
    path = Path(txt_path)
    if path.suffix != ".txt":
        raise ValueError("Dateiendung muss .txt sein.")
    return str(path.with_suffix(".tex"))

def to_pdf(txt_path: str) -> str:
    """Gibt den Pfad zur .pdf-Datei zurück, basierend auf einem .txt-Pfad."""
    path = Path(txt_path)
    if path.suffix != ".txt":
        raise ValueError("Dateiendung muss .txt sein.")
    return str(path.with_suffix(".pdf"))
