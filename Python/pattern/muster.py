import re

def ersetze_mapping_tokens(tokens: list[str], mapping: dict) -> list[str]:
    """Ersetzt alle Mapping-Tokens wie ZEILENSTART, SPACE, ... durch ihre Regex-Entsprechung."""
    return [mapping.get(token, token) for token in tokens]


def ersetze_keys(tokens: list[str], eintrag: dict) -> list[str]:
    """Ersetzt alle Tokens wie KEY1, KEY2, ... durch re.escape() ihrer Werte."""
    def ersetze_token(token):
        if re.fullmatch(r"KEY\d+", token):
            wert = eintrag.get(token, eintrag.get("name", ""))
            return re.escape(wert)
        return token

    return [ersetze_token(token) for token in tokens]



def ersetze_platzhalter(tokens: list[str]) -> list[str]:
    """Ersetzt Platzhalter #1, #2, ... durch Regex-Gruppen (.*?)."""
    return [re.sub(r'#\d+', r'(.*?)', token) for token in tokens]

def generiere_regex(vorlagen: dict, mapping: dict, musterdaten: dict) -> dict:
    """
    Erzeugt aus den geladenen JSON-Daten ein Dict mit benannten Regex-Mustern.
    Rückgabe: {mustername: regex_str}
    """
    muster_dict = {}

    for typ in ['environment', 'command']:
        for eintrag in musterdaten.get(typ, []):
            name = eintrag.get("name")
            vorlage_name = eintrag.get("vorlage")
            if not name or not vorlage_name:
                continue

            # Schritt 1: Vorlage in Tokenliste zerlegen
            tokens = vorlagen[typ][vorlage_name].split()

            # Schritt 2: Verarbeitungsschritte
            tokens = ersetze_mapping_tokens(tokens, mapping)
            tokens = ersetze_keys(tokens, eintrag)
            tokens = ersetze_platzhalter(tokens)

            # Schritt 3: Rückgabe als zusammengebauter Regex (ohne Leerzeichen dazwischen)
            muster_dict[name] = ''.join(tokens)

    return muster_dict
