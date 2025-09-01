from processes.command_bedingung import bedingte_env  

def test_bedingte_env_standard():
    eingabe = {
        "command": [
            {"name": "kompilieren", "environment": "latex"},
            {"name": "rendern", "environment": "html"},
            {"name": "testen", "environment": "python"}
        ]
    }
    erwartet = {
        "kompilieren": "latex",
        "rendern": "html",
        "testen": "python"
    }
    assert bedingte_env(eingabe) == erwartet

def test_bedingte_env_ohne_environment():
    eingabe = {
        "command": [
            {"name": "kompilieren"},
            {"name": "rendern", "environment": "html"}
        ]
    }
    erwartet = {
        "rendern": "html"
    }
    assert bedingte_env(eingabe) == erwartet

def test_bedingte_env_leere_liste():
    eingabe = {
        "command": []
    }
    assert bedingte_env(eingabe) == {}

def test_bedingte_env_keine_command_key():
    eingabe = {}
    assert bedingte_env(eingabe) == {}

def test_bedingte_env_none_werte():
    eingabe = {
        "command": [
            {"name": None, "environment": "latex"},
            {"name": "build", "environment": None}
        ]
    }
    assert bedingte_env(eingabe) == {}
