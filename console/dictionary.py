class Dictionary:
    def __init__(self, values=None):
        self.value = dict(values) if values is not None else {}

    def get(self, key, default=None):
        return self.value.get(key, default)

    def set(self, key, value):
        self.value[key] = value
        return self

    def keys(self):
        return list(self.value.keys())

    def values(self):
        return list(self.value.values())

    def items(self):
        return list(self.value.items())

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Dictionary({self.value!r})"

    def to_python(self):
        return self.value
