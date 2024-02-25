import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(10)  # Exceeding the capacity should raise a ValueError

def test_withdraw():
    jar = Jar()
    jar.deposit(8)

    jar.withdraw(3)
    assert jar.size == 5  # After withdrawing 3 cookies, there should be 5 left

    with pytest.raises(ValueError):
        jar.withdraw(7)  # Withdrawing more than the size should raise a ValueError
