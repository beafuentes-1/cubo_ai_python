"""Calculadora de dos números para ejecutar con Python 3 en la terminal."""
import math


def pedir_numero(mensaje):
    """Repite la pregunta hasta recibir un número válido y finito."""
    while True:
        try:
            numero = float(input(mensaje).strip().replace(",", "."))
            if not math.isfinite(numero):
                print("Escribe un número finito.")
                continue
            return numero
        except ValueError:
            print("Escribe un número válido, por ejemplo: 12 o 3.5.")


def main():
    print("CALCULADORA")
    primero = pedir_numero("Introduce el primer número: ")
    segundo = pedir_numero("Introduce el segundo número: ")

    print("\nElige una operación:")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Potencia (**): primer número elevado al segundo")
    print("6. Resto (%): resto de dividir el primero entre el segundo")
    print("7. División entera (//): cociente redondeado hacia abajo")
    print("8. Raíz: raíz del primer número con índice igual al segundo")

    opciones = {
        "1": "+", "+": "+", "sumar": "+",
        "2": "-", "-": "-", "restar": "-",
        "3": "*", "*": "*", "multiplicar": "*",
        "4": "/", "/": "/", "dividir": "/",
        "5": "**", "**": "**", "potencia": "**",
        "6": "%", "%": "%", "resto": "%",
        "7": "//", "//": "//", "division entera": "//",
        "8": "raiz", "raiz": "raiz", "raíz": "raiz",
    }
    while True:
        eleccion = input("Operación (número, símbolo o nombre): ").strip().lower()
        if eleccion in opciones:
            operacion = opciones[eleccion]
            break
        print("Operación inválida. Elige una opción del 1 al 8.")

    try:
        if operacion in ("/", "//", "%") and segundo == 0:
            print("No puedes dividir ni calcular el resto entre cero.")
            return

        if operacion == "+":
            resultado = primero + segundo
        elif operacion == "-":
            resultado = primero - segundo
        elif operacion == "*":
            resultado = primero * segundo
        elif operacion == "/":
            resultado = primero / segundo
        elif operacion == "**":
            resultado = primero ** segundo
        elif operacion == "%":
            resultado = primero % segundo
        elif operacion == "//":
            resultado = primero // segundo
        else:
            if segundo == 0:
                print("El índice de la raíz no puede ser cero.")
                return
            if primero < 0:
                if not segundo.is_integer() or segundo % 2 == 0:
                    print("Para un número negativo, usa un índice entero impar.")
                    return
                resultado = -((-primero) ** (1 / segundo))
            else:
                resultado = primero ** (1 / segundo)

        if isinstance(resultado, complex):
            print(f"Resultado complejo: {resultado}")
        elif not math.isfinite(resultado):
            print("El resultado excede el rango numérico de esta calculadora.")
        else:
            print(f"Resultado: {resultado:g}")
    except ZeroDivisionError:
        print("No se puede elevar cero a una potencia negativa.")
    except (OverflowError, ValueError):
        print("No se puede calcular ese resultado con los números ingresados.")


# Este bloque ejecuta la calculadora al abrir el archivo desde la terminal.
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nCalculadora cerrada.")