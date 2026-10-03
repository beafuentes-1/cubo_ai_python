class Tuple:
    def __init__(self, values=None):
        self.value = tuple(values) if values is not None else tuple()

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Tuple({self.value!r})"

    def to_python(self):
        return self.value


# Ejercicios didácticos para Tuple

def ejercicio_1_crear_tupla():
    """Crea una tupla con tres elementos."""
    return ("Python", "Java", "C++")


def ejercicio_2_acceder_elemento(tupla):
    """Accede al segundo elemento de una tupla."""
    return tupla[1]


def ejercicio_3_longitud(tupla):
    """Devuelve la longitud de una tupla."""
    return len(tupla)


def ejercicio_4_sumar_tuplas(a, b):
    """Concatena dos tuplas."""
    return a + b


def ejercicio_5_contar_elemento(tupla, valor):
    """Cuenta cuántas veces aparece un valor."""
    return tupla.count(valor)


if __name__ == "__main__":
    print("Ejercicio 1:", ejercicio_1_crear_tupla())
    print("Ejercicio 2:", ejercicio_2_acceder_elemento(("a", "b", "c")))
    print("Ejercicio 3:", ejercicio_3_longitud((10, 20, 30, 40)))
    print("Ejercicio 4:", ejercicio_4_sumar_tuplas((1, 2), (3, 4)))
    print("Ejercicio 5:", ejercicio_5_contar_elemento((1, 2, 2, 3, 2), 2))
