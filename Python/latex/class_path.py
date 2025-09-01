import os
import re

import os
import re

def class_to_text(text: str, pfad_zur_klasse: str) -> str:
    """
    Fügt einen LaTeX-Block mit makeatletter def input@path{{...}} makeatother
    vor der documentclass-Zeile ein, um das Klassenverzeichnis anzugeben.
    """
    # Pfad für LaTeX vorbereiten (mit Slashes und doppelten geschweiften Klammern)
    pfad = os.path.abspath(pfad_zur_klasse).replace('\\', '/')
    input_path_block = (
        f"\\makeatletter\n"
        f"\\def\\input@path{{{{{pfad}/}}}}\n"
        f"\\makeatother\n\n"
    )

    # Suchen der documentclass-Zeile
    pattern = r"(\\documentclass(?:\[[^\]]*\])?\{[^}]+\})"

    match = re.search(pattern, text)
    if match:
        start = match.start()
        # Block davor einfügen
        return text[:start] + input_path_block + text[start:]
    else:
        # Wenn keine documentclass-Zeile gefunden wird, bleibt der Text unverändert
        return text

