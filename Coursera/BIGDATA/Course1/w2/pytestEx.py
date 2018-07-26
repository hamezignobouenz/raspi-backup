import pytest

def get_words(input_line):
    return input_line.split()

def test_get_words_simple_string():
    assert get_words("a b dc efg") == ["a","b","dc", "efg"]

def test_get_words_parse_empty():
    assert get_words("") == []

def test_get_words_exceptionnoinput():
    with pytest.raises(AttributeError):
        get_words(None)
