class Integer:
    def __init__(self, value: int = 0):
        self.value = int(value)

    @staticmethod
    def _as_int(value):
        if isinstance(value, Integer):
            return value.value
        return int(value)

    def __add__(self, other):
        return Integer(self.value + self._as_int(other))

    def __sub__(self, other):
        return Integer(self.value - self._as_int(other))

    def __mul__(self, other):
        return Integer(self.value * self._as_int(other))

    def __truediv__(self, other):
        return Float(self.value / self._as_int(other))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Integer({self.value!r})"

    def to_python(self):
        return self.value


from .float import Float
