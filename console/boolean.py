class Boolean:
    def __init__(self, value: bool = False):
        self.value = bool(value)

    def __bool__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Boolean({self.value!r})"

    def __eq__(self, other):
        if isinstance(other, Boolean):
            return self.value == other.value
        return self.value == bool(other)

    def to_python(self):
        return self.value


if __name__ == "__main__":
    print(Boolean(True))
    print(Boolean(False))
