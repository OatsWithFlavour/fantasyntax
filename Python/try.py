import re
from typing import Dict
from log.logger import log_call

@log_call
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
    return {k: re.sub(muster, ersatz, v) for k, v in klammer_expressions.items()}

def retransform(mapping: Dict[int, str]) -> str:
    """
    Rekonstruiert den Ausdruck aus dem Dictionary mit den (#index)-Platzhaltern.
    """
    text = mapping[max(mapping.keys())]
    pattern = re.compile(r"#(\d+)")

    while re.search(pattern, text):
        text = re.sub(pattern, lambda m: mapping[int(m.group(1))], text)

    return text

def ersetze_klammern(text: str, muster: str, ersatz: str) -> str:
    """
    Gesamtfunktion: transformiert den Ausdruck, ersetzt mit Regex, baut zurück.
    """
    mapping = transform(text)
    mapping = ersetze(mapping, muster, ersatz)
    return retransform(mapping)


text = '$(a_(s) + wurzel(b + c_(g + d)))/(a + b(c))$'
muster = r"wurzel\((.*?)\)"
muster2 = r"\((.*?)\)/\((.*?)\)"
ersatz = r"sqrt{\1}"
ersatz2 = r"\\frac{\1}{\2}"
ausgabe = ersetze_klammern(text, muster, ersatz)
ausgabe = ersetze_klammern(ausgabe, muster2, ersatz2)
print(ausgabe)
