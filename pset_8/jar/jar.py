class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Initially, the cookie jar is empty

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer")

        if self._size + n > self._capacity:
            raise ValueError("Deposit would exceed the cookie jar's capacity")

        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer")

        if n > self._size:
            raise ValueError(
                "Withdrawal exceeds the number of cookies in the cookie jar"
            )

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(5)

    print(jar)# Expected output: 🍪🍪🍪🍪🍪


if __name__ == "__main__":
    main()
