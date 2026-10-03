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
mensaje = f"{nombre}, tienes {edad} años."
