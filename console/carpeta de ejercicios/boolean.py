# BOOLEAN: valores lógicos (tipo bool)
# Una comparación devuelve True (verdadero) o False (falso).

# input pide datos por consola y devuelve texto.
nombre = input("¿Cómo te llamas? ").strip()

# Convertimos la edad a int para poder comparar números.
# Si se escribe un dato inválido, volvemos a pedirlo.
while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad < 0:
            print("La edad no puede ser negativa.")
            continue
        break
    except ValueError:
        print("Escribe tu edad como un número entero, por ejemplo: 18.")

# < significa «menor que».
if edad < 18:
    print(f"{nombre}, eres menor de edad.")
else:
    print(f"{nombre}, eres mayor de edad.")

# == compara dos valores; = asigna un valor a una variable.
es_igual_a_18 = edad == 18

# Mostramos dos mensajes: el valor de Python y su equivalente en español.
print(f"¿Tu edad es igual a 18? {es_igual_a_18}")
if es_igual_a_18:
    print("Resultado en español: verdadero.")
else:
    print("Resultado en español: falso.")
