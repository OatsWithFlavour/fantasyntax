import re
from typing import Dict

def transform(text: str) -> Dict[int, str]:
    """
    Zerlegt den Text rekursiv und ersetzt die innersten Klammern durch nummerierte Platzhalter.
    """
    stack = []
    mapping = {}
    idx = 0

    def replace_match(match):
        nonlocal idx
        content = match.group(1)
        mapping[idx] = content
        placeholder = f"#{idx}"
        idx += 1
        return placeholder

    pattern = re.compile(r"\(([^()]+)\)")
    while re.search(pattern, text):
        text = re.sub(pattern, replace_match, text)

    mapping[idx] = text

    # Ersetze #Zahl durch (#Zahl) in allen Dictionary-Werten
    placeholder_pattern = re.compile(r"#(\d+)")
    for key in mapping:
        mapping[key] = placeholder_pattern.sub(r"(#\1)", mapping[key])

    return mapping



def ersetze(klammer_expressions: Dict[int, str], muster: str, ersatz: str) -> Dict[int, str]:
    """
    Regex-Ersetzung auf allen gespeicherten Ausdrücken im Dictionary.
    """
    return {k: re.sub(muster, ersatz, v, flags=re.MULTILINE | re.DOTALL) for k, v in klammer_expressions.items()}


def retransform(mapping: Dict[int, str]) -> str:
    """
    Rekonstruiert den Ausdruck aus dem Dictionary mit den (#index)-Platzhaltern.
    Schützt vor Endlosschleifen und fehlenden Einträgen.
    """
    text = mapping[max(mapping.keys())]
    pattern = re.compile(r"#(\d+)")
    max_iterations = 1000
    iteration = 0

    while pattern.search(text):
        if iteration > max_iterations:
            raise RuntimeError("Maximale Rekursionstiefe bei retransform erreicht – mögliche Endlosschleife.")
        
        def ersetze_platzhalter(match):
            key = int(match.group(1))
            if key not in mapping:
                raise KeyError(f"Platzhalter #{key} nicht im Mapping gefunden.")
            return mapping[key]
        
        text = pattern.sub(ersetze_platzhalter, text)
        iteration += 1

    return text


def ersetze_klammern(text: str, muster: str, ersatz: str) -> str:
    """
    Gesamtfunktion: transformiert den Ausdruck, ersetzt mit Regex, baut zurück.
    """
    mapping = transform(text)
    mapping = ersetze(mapping, muster, ersatz)
    return retransform(mapping)


