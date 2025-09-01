import re
from pattern.muster import (
    ersetze_mapping_tokens,
    ersetze_keys,
    ersetze_platzhalter,
    generiere_regex
)

def test_ersetze_mapping_tokens():
    tokens = ["ZEILENSTART", "abc", "ZEILENENDE"]
    mapping = {"ZEILENSTART": "^", "ZEILENENDE": "$"}
    assert ersetze_mapping_tokens(tokens, mapping) == ["^", "abc", "$"]

def test_ersetze_keys():
    tokens = ["KEY1", "und", "KEY2"]
    eintrag = {"KEY1": "a+b", "KEY2": "c.d"}
    result = ersetze_keys(tokens, eintrag)
    assert result == [re.escape("a+b"), "und", re.escape("c.d")]

def test_ersetze_platzhalter():
    tokens = ["abc", "#1", "#2", "def"]
    result = ersetze_platzhalter(tokens)
    assert result == ["abc", "(.*?)", "(.*?)", "def"]

def test_generiere_regex():
    vorlagen = {
        "environment": {
            "test_vorlage": "ZEILENSTART KEY1 #1 KEY2"
        }
    }
    mapping = {
        "ZEILENSTART": "^"
    }
    eintrag = {
        "environment": [
            {
                "name": "test_muster",
                "vorlage": "test_vorlage",
                "KEY1": "123",
                "KEY2": "456"
            }
        ],
        "command": []
    }
    result = generiere_regex(vorlagen, mapping, eintrag)
    assert result == {"test_muster": "^123(.*?)456"}
