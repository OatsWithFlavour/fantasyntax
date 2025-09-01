import sys
from pathlib import Path

def listen_textpath() -> str:
    """Liefert den übergebenen Pfad zur .txt-Datei als String zurück"""
    if len(sys.argv) < 2:
        raise ValueError("Es wurde kein Pfad zur .txt-Datei übergeben.")
    
    pfad = Path(sys.argv[1])
    
    if not pfad.exists():
        raise FileNotFoundError(f"Die Datei existiert nicht: {pfad}")
    if pfad.suffix != ".txt":
        raise ValueError(f"Die Datei ist keine .txt-Datei: {pfad}")
    
    return str(pfad.resolve())
