class Complex:
    def __init__(self, value: complex = 0 + 0j):
        self.value = complex(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Complex({self.value!r})"

    def conjugate(self):
        return Complex(self.value.conjugate())

    def magnitude(self):
        return abs(self.value)

    @property
    def real_part(self):
        return self.value.real

    @property
    def imag_part(self):
        return self.value.imag

    def to_python(self):
        return self.value


if __name__ == "__main__":
    z = Complex(3 + 4j)
    print(z)
    print(z.magnitude())
