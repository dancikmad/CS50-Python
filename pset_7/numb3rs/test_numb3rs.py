from numb3rs import validate
import pytest


def test_valid_ip_format():
    """A function that tests if the input matches the correct format of ip address

    - Correct Format: #.#.#.# (# - a number between 0 and 255)
    """
    # Expected output - True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

    # Expected output - False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("1.4.2") == False
    assert validate("127.3.4") == False
    assert validate("127.1000.1000.1000") == False


def test_non_digits():
    """A function that tests if the input has at least 1 non-digit character"""

    assert validate("cat") == False
    assert validate("ip.0.0.1") == False

def test_firstbyte():
    assert validate('127.1000.1000.512') == False
    assert validate('101.512.250.297') == False

