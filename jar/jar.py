class Jar:
    def __init__(self, capacity=12):
        try:
            if type(capacity) == int and capacity >= 0:
                self.capacity = capacity
                self.size = 0
            else:
                raise ValueError("Capacity must be non-negative")
        except TypeError:
            raise ValueError("Capacity must be a int")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        try:
            if self.size + n > self.capacity:
                raise ValueError("Too many cookies")
            else:
                self.size += n
        except TypeError:
            print("Must be a number")


    def withdraw(self, n):
        try:
            if self.size < n:
                raise ValueError("Not enough cookies")
            else:
                self.size -= n
        except TypeError:
            print("Must be a number")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, other):
        self._capacity = other

    @size.setter
    def size(self, other):
        self._size = other
