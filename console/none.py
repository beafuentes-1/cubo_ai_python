class NoneValue:
    def __bool__(self):
        return False

    def __str__(self):
        return "None"

    def __repr__(self):
        return "NoneValue()"

    def to_python(self):
        return None
