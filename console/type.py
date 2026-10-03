# TYPE: identificar el tipo de un dato
# type() es una función que devuelve el tipo de un valor.
# No es un tipo de dato por sí misma.

# 1. Tipos de datos básicos.
nombre = "Ana"
edad = 18
altura = 1.65
es_estudiante = True

print("Nombre:", nombre, "| Tipo:", type(nombre))
print("Edad:", edad, "| Tipo:", type(edad))
print("Altura:", altura, "| Tipo:", type(altura))
print("Es estudiante:", es_estudiante, "| Tipo:", type(es_estudiante))

# 2. Tipos de colecciones.
frutas = ["manzana", "pera"]
coordenadas = (10, 20)
persona = {"nombre": "Ana", "edad": 18}
numeros = {1, 2, 3}

print("Frutas:", type(frutas))          # list
print("Coordenadas:", type(coordenadas))  # tuple
print("Persona:", type(persona))        # dict
print("Números:", type(numeros))        # set

# 3. Otros tipos.
resultado = None
numero_complejo = 3 + 2j
datos = b"Hola"

print("Resultado:", type(resultado))       # NoneType
print("Número complejo:", type(numero_complejo))  # complex
print("Datos:", type(datos))               # bytes

# 4. Mostrar solamente el nombre del tipo.
print("Tipo de edad:", type(edad).__name__)  # int

# 5. Pedir datos por consola.
# input() siempre devuelve texto, aunque escribas un número.
entrada = input("Escribe tu edad: ")

print("Valor recibido:", entrada)
print("Tipo antes de convertir:", type(entrada))  # str

# Intentamos convertir el texto a un número entero.
try:
    edad_convertida = int(entrada)
    print("Edad convertida:", edad_convertida)
    print("Tipo después de convertir:", type(edad_convertida))  # int
except ValueError:
    print("No se puede convertir ese texto a un número entero.")

# 6. Comprobar el tipo exacto de un valor.
es_entero = type(edad) is int
print("¿La variable edad es de tipo int?", es_entero)  # True

# Ejercicio:
# Crea tres variables: tu nombre, tu edad y tu altura.
# Muestra el valor y el tipo de cada una usando print() y type().