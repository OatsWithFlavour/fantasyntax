from processes.substitution import suche_muster, ersetze, rekombiniere, substituiere, sub_klammern

def test_suche_muster():
    text = "abc 123 abc 456"
    muster = r"abc \d+"
    result = suche_muster(text, muster)
    assert result == [(0, 7), (8, 15)]

def test_ersetze():
    text = "abc 123 abc 456"
    muster = r"\d+"
    ersatz = "###"
    result = ersetze(text, muster, ersatz)
    assert result == "abc ### abc ###"

def test_rekombiniere():
    text = "abcdefghij"
    ersetzungen = [(2, 5, "XYZ"), (7, 9, "Q")]
    result = rekombiniere(text, ersetzungen)
    assert result == "abXYZfgQj"

def test_substituiere():
    text = "Start [a = 1, b = 2] End\nStart [c = 3] End"
    äußeres_muster = r"Start \[.*?\] End"
    inneres_muster = r"\d+"
    innerer_ersatz = "X"
    result = substituiere(text, äußeres_muster, inneres_muster, innerer_ersatz)
    expected = "Start [a = X, b = X] End\nStart [c = X] End"
    assert result == expected

def test_sub_klammern_ohne_klammer():
    text = "Wert = 123"
    muster = r"\d+"
    ersatz = "X"
    result = sub_klammern(text, muster, ersatz)
    assert result == "Wert = X"  # verwendet ersetze

def test_sub_klammern_mit_klammer(monkeypatch):
    # ersetze_klammern mocken
    def mock_ersetze_klammern(text, muster, ersatz):
        return "MOCKED"

    monkeypatch.setattr("processes.substitution.ersetze_klammern", mock_ersetze_klammern)
    text = "(a + b)"
    muster = r"a|b"
    ersatz = "X"
    result = sub_klammern(text, muster, ersatz)
    assert result == "MOCKED"
