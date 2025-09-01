import re

def ersetze_values(tokens: list[str], eintrag: dict) -> list[str]:
    """Ersetzt alle Tokens wie VAL1, VAL2, ... durch ihre konkreten Werte (nicht escaped)."""
    def ersetze_token(token):
        if re.fullmatch(r"VAL\d+", token):
            return eintrag.get(token, eintrag.get("name", ""))
        return token

    return [ersetze_token(token) for token in tokens]

def ersetze_platzhalter(tokens: list[str]) -> list[str]:
    """Ersetzt Platzhalter #1, #2, ... durch \\1, \\2, ... (für Ersatz-Strings)."""
    return [re.sub(r'#(\d+)', r'\\\1', token) for token in tokens]

def generiere_ersatz(vorlagen: dict, ersatzdaten: dict) -> dict:
    """
    Erzeugt aus den geladenen JSON-Daten ein Dict mit benannten Ersatz-Strings.
    Rückgabe: {ersatzname: ersatz_str}
    """
    ersatz_dict = {}

    for typ in ['environment', 'command']:
        for eintrag in ersatzdaten.get(typ, []):
            name = eintrag.get("name")
            vorlage_name = eintrag.get("vorlage")
            if not name or not vorlage_name:
                continue

            schablone = vorlagen.get(typ, {}).get(vorlage_name)
            if not schablone:
                continue
            tokens = schablone.split()

            tokens = ersetze_values(tokens, eintrag)
            tokens = ersetze_platzhalter(tokens)

            ersatz_dict[name] = ''.join(tokens)

    return ersatz_dict
