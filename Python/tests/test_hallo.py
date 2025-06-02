from processes import hallo


def test_hallo():
    result = hallo.hallo()
    assert result == "hallo"
