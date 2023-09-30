from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_nums():
    assert shorten("12345") == "12345"
    assert shorten("a1B2c3") == "1B2c3"

def test_symbols():
    assert shorten(".,?<>/[]") == ".,?<>/[]"

