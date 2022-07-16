class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError ("Jar is empty")
        self._capacity=capacity #the underscore in self._capacity is extremely important or python will not be able to set attribute "capacity"
        self._size = 0 #the underscore is extremely important

    def __str__(self):
        cookie = ""
        while self._size > 0:
            self._size = self._size - 1
            cookie = cookie + "🍪"
        return cookie

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Jar is full")
        if self._size + n > self._capacity:
            raise ValueError("Jar is full")
        self._size += n #== self.size

    def withdraw(self, n):
        if n > self._size:
            raise ValueError ("Not enough cookies in jar")
        if n > self._capacity:
            raise ValueError ("Not enough cookies in jar")
        self._size -= n #underscore

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size #the underscore is extremely important
'''
this wont work. you need an underscore
    @property
    def capacity(self):
        return self.capacity
    @property
    def size(self):
        return self.size
'''

jar = Jar()
jar.deposit(-2)
#jar.withdraw(5)
print(jar)
