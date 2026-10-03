class List:
    def __init__(self, values=None):
        self.value = list(values) if values is not None else []

    def append(self, item):
        self.value.append(item)
        return self

    def extend(self, items):
        self.value.extend(items)
        return self

    def pop(self, index=-1):
        return self.value.pop(index)

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"List({self.value!r})"

    def to_python(self):
        return self.value
