from working import convert
import pytest


def test_valid_inputs():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_omit_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_out_range_times():
    """Tests for hrs / minutes out of range time"""
    with pytest.raises(ValueError):
        convert("9:65 AM to 26:00 PM")
