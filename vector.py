#! python3

class Vector:
    def __init__(self, x, y):
        self._x = int(x)
        self._y = int(y)
        temp = (self._x**2 + self._y**2)**0.5
        self._vlen = round(temp, 5)

    def __str__(self):
        return f'V({self._x}, {self._y})'

    def __len__(self):
        return int(round(self._vlen, 0))

    def __eq__(a, b):
        return a._x == b._x and a._y == b._y

    def __ne__(a, b):
        return not (a == b)

    def __lt__(a, b):
        return a._vlen < b._vlen

    def __le__(a, b):
        return a._vlen <= b._vlen

    def __gt__(a, b):
        return a._vlen > b._vlen

    def __ge__(a, b):
        return a._vlen >= b._vlen

    def __add__(a, b):
        return Vector(a._x + b._x, a._y + b._y)

    def __mul__(a, n):
        if isinstance(n, Vector):
            return a._x * b._x + a._y * b._y
        return Vector(a._x * n, a._y * n)

    def __neg__(a):
        return a * -1

    def __iadd__(a, b):
        return a + b

    def __sub__(a, b):
        return a + -b

    def __isub__(a, b):
        return a + -b

    def __rmul__(a, n):
        return a * n

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def scalar(a, b):
        return a * b

    def cos(a, b):
        return round((a * b) / (a._vlen * b._vlen), 5)


a = Vector(1, 2)
b = Vector(3, 4)
print(a, b)
print(a == b)
print(a != b)
print(a + b)
print(a - b)
print(a * 3)
print(4 * a)
a += b
print(a)  # V(4, 6)
a -= Vector(1, 1)
print(a)  # (3, 5)
print("len(a) =", len(a))
print("len(b) =", len(b))
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(b.getX(), b.getY())
print(a.scalar(b))  # 29
print(a.cos(b))  # ≈ 0.99469
