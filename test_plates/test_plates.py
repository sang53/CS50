from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("aAAAaAAA") == False
    assert is_valid("AAAAA") == True

def test_startsalpha():
    assert is_valid("12234") == False
    assert is_valid("A132") == False
    assert is_valid("1a234") == False

def test_0startnum():
    assert is_valid("AA0123") == False
    assert is_valid("AA1123") == True

def test_endsnum():
    assert is_valid("aA123A") == False
    assert is_valid("AA1234") == True

def test_symb():
    assert is_valid(".,?/[]") == False
    assert is_valid("aw.,?") == False
    assert is_valid("aw123.") == False