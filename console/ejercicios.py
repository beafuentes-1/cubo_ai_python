"""Ejercicios didácticos para la carpeta console.

Objetivo: practicar variables, tipos de datos, listas, diccionarios,
condicionales y funciones básicas en Python.
"""


def ejercicio_1_suma():
    """Crea dos números y devuelve su suma."""
    a = 10
    b = 5
    return a + b


def ejercicio_2_lista_invertida(lista):
    """Devuelve una lista invertida."""
    return lista[::-1]


def ejercicio_3_diccionario_usuario(nombre, edad):
    """Crea un diccionario con nombre y edad."""
    return {"nombre": nombre, "edad": edad}


def ejercicio_4_es_par(numero):
    """Indica si un número es par."""
    return numero % 2 == 0


def ejercicio_5_mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números."""
    return max(a, b, c)


def ejercicio_6_contar_vocales(texto):
    """Cuenta cuántas vocales tiene un texto."""
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)


if __name__ == "__main__":
    print("Ejercicio 1:", ejercicio_1_suma())
    print("Ejercicio 2:", ejercicio_2_lista_invertida([1, 2, 3, 4]))
    print("Ejercicio 3:", ejercicio_3_diccionario_usuario("Ana", 21))
    print("Ejercicio 4:", ejercicio_4_es_par(8))
    print("Ejercicio 5:", ejercicio_5_mayor_de_tres(4, 9, 2))
    print("Ejercicio 6:", ejercicio_6_contar_vocales("programacion"))
