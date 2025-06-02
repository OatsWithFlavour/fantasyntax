import pytest
from helper.io import TextFile

def test_write_and_read(tmp_path):
    file = tmp_path / "testfile.txt"
    text_file = TextFile(file)

    content = "Dies ist ein Test."
    text_file.write(content)
    
    result = text_file.read()
    assert result == content

def test_read_missing_file(tmp_path):
    file = tmp_path / "nicht_vorhanden.txt"
    text_file = TextFile(file)

    with pytest.raises(FileNotFoundError):
        _ = text_file.read()
