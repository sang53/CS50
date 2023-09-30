from working import convert
import pytest

def test_outofrange():
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("8:60 PM to 8:61 PM")


def test_wrongformat():
    with pytest.raises(ValueError):
        convert("8PM to 9AM")
    with pytest.raises(ValueError):
        convert ("8:30PM to 9AM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("8:30PM to 9AM")
    with pytest.raises(ValueError):
        convert("8 PM - 9 AM")
    with pytest.raises(ValueError):
        convert("8:30 PM 9:00 AM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM 8 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

def test_working():
    assert convert("8 AM to 9 PM") == "08:00 to 21:00"
    assert convert("8:30 AM to 9:25 PM") == "08:30 to 21:25"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"