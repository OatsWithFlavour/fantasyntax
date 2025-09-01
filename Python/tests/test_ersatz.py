from pattern.ersatz import ersetze_values, ersetze_platzhalter, generiere_ersatz

def test_ersetze_values():
    tokens = ["VAL1", "und", "VAL2"]
    eintrag = {"VAL1": "Haus", "VAL2": "Baum"}
    assert ersetze_values(tokens, eintrag) == ["Haus", "und", "Baum"]

def test_ersetze_platzhalter():
    tokens = ["abc", "#1", "#2"]
    assert ersetze_platzhalter(tokens) == ["abc", r"\1", r"\2"]

def test_generiere_ersatz():
    vorlagen = {
        "environment": {"env1": "VAL1 #1 VAL2"},
        "command": {}
    }
    ersatzdaten = {
        "environment": [ {
            "name": "mein_env",
            "vorlage": "env1",
            "VAL1": "a",
            "VAL2": "b"
        }],
        "command": []
    }
    result = generiere_ersatz(vorlagen, ersatzdaten)
    assert result["mein_env"] == "a\\1b"

