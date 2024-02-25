from twttr import shorten

def test_capital_letters():
    assert shorten("BTC") == "BTC"
    assert shorten ("CS") == "CS"

def test_punctuation():
    assert shorten("10.00 dollars") == "10.00 dllrs"

def test_vowels():
    assert shorten('eau') == ''

def test_consonants():
    assert shorten('ggp') == 'ggp'

def test_words_ommiting_vowels():
    assert shorten('Python CS 50 course') == 'Pythn CS 50 crs'
    assert shorten('house') == 'hs'
    assert shorten('SeaSide') == 'SSd'
    assert shorten('HONG KONG') == 'HNG KNG'



