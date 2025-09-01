from pattern.klammer_expression import (
    transform,
    ersetze,
    retransform,
    ersetze_klammern
)

def test_transform():
    text = '$(a_(s) + wurzel(b + c_(g + d)))/(a + b(c))$'
    mapping = transform(text)

    assert isinstance(mapping, dict)
    assert max(mapping.keys()) in mapping
    assert "#0" not in mapping[max(mapping.keys())]  # sollte (#0) sein
    assert any(f"(#{"0"})" in v or f"(#{"1"})" in v for v in mapping.values())

def test_ersetze_wurzel():
    text = 'wurzel(a + b)'
    mapping = {0: 'wurzel(a + b)'}
    muster = r"wurzel\((.*?)\)"
    ersatz = r"sqrt{\1}"
    result = ersetze(mapping, muster, ersatz)
    assert result[0] == 'sqrt{a + b}'

def test_ersetze_bruch():
    mapping = {0: '(a + b)/(c + d)'}
    muster = r"\((.*?)\)/\((.*?)\)"
    ersatz = r"\\frac{\1}{\2}"
    result = ersetze(mapping, muster, ersatz)
    assert result[0] == r'\frac{a + b}{c + d}'

def test_retransform():
    mapping = {
        0: 'c',
        1: 'b + (#0)',
        2: 'a + (#1)'
    }
    result = retransform(mapping)
    assert result == 'a + (b + (c))'

def test_ersetze_klammern_end_to_end():
    text = '$(a_(s) + wurzel(b + c_(g + d)))/(a + b(c))$'
    muster1 = r"wurzel\((.*?)\)"
    ersatz1 = r"sqrt{\1}"
    muster2 = r"\((.*?)\)/\((.*?)\)"
    ersatz2 = r"\\frac{\1}{\2}"

    result = ersetze_klammern(text, muster1, ersatz1)
    result = ersetze_klammern(result, muster2, ersatz2)

    assert "sqrt{" in result
    assert r"\frac{" in result
    assert "(g + d)" in result  # Tiefstes Glied sollte erhalten bleiben

