from numb3rs import validate

def test_nonnums():
    assert validate("a.b.c.d") == False
    assert validate("/.?.m.4") == False


def test_range():
    assert validate("265.5.3.2") == False
    assert validate("0.366.435.654") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_regex():
    assert validate("cat") == False
    assert validate("....") == False
    assert validate("0..0.0.0") == False