import re


def ersetze_mapping_tokens(schablone: str, mapping: dict) -> str:
    """Ersetzt alle Tokens wie ZEILENSTART, SPACE, ... durch ihre Regex-Entsprechung."""
    for token, regex in mapping.items():
        schablone = schablone.replace(token, regex)
    return schablone


def ersetze_keys(schablone: str, eintrag: dict) -> str:
    """Ersetzt alle Schlüssel wie KEY1, KEY2, ... durch deren konkrete Werte (escaped)."""
    for key, value in eintrag.items():
        if key.startswith("KEY"):
            schablone = schablone.replace(key, re.escape(value))
    return schablone


def ersetze_platzhalter(schablone: str) -> str:
    """Ersetzt Platzhalter #1, #2, ... durch Regex-Gruppen, die auch mehrzeilig matchen."""
    return re.sub(r'#\d+', r'(.*?)', schablone)


def bereinige_regex(schablone: str) -> str:
    """Entfernt überflüssige Leerzeichen aus dem Regex."""
    return schablone.replace(" ", "")


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

            schablone = vorlagen[typ][vorlage_name]
            schablone = bereinige_regex(schablone)
            schablone = ersetze_mapping_tokens(schablone, mapping)
            schablone = ersetze_keys(schablone, eintrag)
            regex = ersetze_platzhalter(schablone)

            muster_dict[name] = regex

    return muster_dict
