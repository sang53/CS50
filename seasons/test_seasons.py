from seasons import convert
import pytest
from datetime import date

def test_format():
    with pytest.raises(SystemExit):
        convert("abcd123")
    with pytest.raises(SystemExit):
        convert("January 1, 1998")
    with pytest.raises(SystemExit):
        convert("01-01-1999")
    with pytest.raises(SystemExit):
        convert("1998-13-32")
    with pytest.raises(SystemExit):
        convert("3023-01-01")

def test_working():
    assert convert("1999-01-01") == date(1999, 1, 1)