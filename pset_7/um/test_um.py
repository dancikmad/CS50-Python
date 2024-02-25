from um import count


def test_substring_um():
    assert count("instrumentation") == 0
    assert count("disequilibrium") == 0
    assert count("circumnavigate") == 0
    assert count("documentation") == 0

def test_word_itself():
    assert count("python um.py") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
