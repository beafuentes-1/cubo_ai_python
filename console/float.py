class Float:
    def __init__(self, value: float = 0.0):
        self.value = float(value)

    @staticmethod
    def _as_float(value):
        if isinstance(value, Float):
            return value.value
        return float(value)

    def __add__(self, other):
        return Float(self.value + self._as_float(other))

    def __sub__(self, other):
        return Float(self.value - self._as_float(other))

    def __mul__(self, other):
        return Float(self.value * self._as_float(other))

    def __truediv__(self, other):
        return Float(self.value / self._as_float(other))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Float({self.value!r})"

    def to_python(self):
        return self.value
