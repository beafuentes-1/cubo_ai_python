class Set:
    def __init__(self, values=None):
        self.value = set(values) if values is not None else set()

    def add(self, item):
        self.value.add(item)
        return self

    def union(self, other):
        return Set(self.value.union(set(other)))

    def intersection(self, other):
        return Set(self.value.intersection(set(other)))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Set({self.value!r})"

    def to_python(self):
        return self.value
