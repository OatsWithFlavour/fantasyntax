import re
from pattern.klammer_expression import ersetze_klammern

def suche_muster(text, muster):
    """Findet alle Vorkommen eines Musters mit Gruppe und gibt (start, end, inhalt) zurück."""
    matches = []
    for m in re.finditer(muster, text, flags=re.MULTILINE | re.DOTALL):
        start, end = m.span()          # Start- und Endposition des Treffers im Originaltext
        matches.append((start, end))
    return matches

def ersetze(text, muster, ersatz):
    """Ersetzt alle Vorkommen des Musters im Text durch den Ersatz."""
    ersetzter_text = re.sub(muster, ersatz, text, flags=re.MULTILINE | re.DOTALL)
    return ersetzter_text

def sub_klammern(text: str, muster: str, ersatz: str) -> str:
    if "(" in text or ")" in text:
        return ersetze_klammern(text, muster, ersatz)
    else:
        return ersetze(text, muster, ersatz)
    
def rekombiniere(text, ersetzungen):
    """Ersetzt im Text alle Bereiche von hinten nach vorne gemäß (start, end, neuer_inhalt)."""
    for start, end, neu in reversed(ersetzungen):
        text = text[:start] + neu + text[end:]  # Ersetze den Textabschnitt durch neuen Inhalt
    return text

def substituiere(text, äußeres_muster, inneres_muster, innerer_ersatz):
    """Ersetzt innere Muster innerhalb äußerer Musterblöcke und setzt den Text neu zusammen."""
    treffer = suche_muster(text, äußeres_muster)
    ersetzungen = []

    for start, end in treffer:
        ersetzter_inhalt = sub_klammern(text[start:end], inneres_muster, innerer_ersatz)
        ersetzungen.append((start, end, ersetzter_inhalt))  # Speichere Ersetzung als Tupel
    return rekombiniere(text, ersetzungen)


