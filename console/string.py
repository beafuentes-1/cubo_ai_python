class String:
    def __init__(self, value: str = ""):
        self.value = str(value)

    def upper(self):
        return String(self.value.upper())

    def lower(self):
        return String(self.value.lower())

    def strip(self):
        return String(self.value.strip())

    def split(self, separator=None):
        return self.value.split(separator)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"String({self.value!r})"

    def to_python(self):
        return self.value
