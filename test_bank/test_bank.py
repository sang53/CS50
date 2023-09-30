from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HeLLo") == 0

def test_hstr():
    assert value("hasdfas") == 20
    assert value("HaDSDFf") == 20

def test_nonhstr():
    assert value("asdf") == 100
    assert value("ASDF") == 100

def test_nums():
    assert value("01234") == 100
    assert value("h2345") == 20
    assert value("H123") == 20

def test_symb():
    assert value("01./?4") == 100
    assert value("h2?>?]5") == 20
    assert value("H 2?>|.") == 20