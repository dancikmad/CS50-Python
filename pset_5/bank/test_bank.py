from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello, world') == 0

def test_with_h():
    assert value('hey') == 20
    assert value('how are you?') == 20
    assert value('hola, como estais!') == 20
    assert value('hi there') == 20

def test_ommiting_h():
    assert value('what are you up to?') == 100
    assert value('do you need help?') == 100

def test_capitals():
    assert value('Hey') == 20
    assert value('HELLO') == 0
    assert value('Are You Sure?') == 100
