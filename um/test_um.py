from um import count

def test_inword():
    assert count("gypsum, Um") == 1
    assert count("um, gypsum") == 1

def test_case():
    assert count("Um, uM, um, UM") == 4

def test_working():
    assert count("hello, um, world um") == 2
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, umm...") == 1
    assert count("hello") == 0
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
