"""Ejercicios didácticos para la carpeta desktop.

Objetivo: practicar interfaces gráficas con Tkinter.
"""

import tkinter as tk


class EjercicioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios Desktop")
        self.root.geometry("320x220")

        self.label = tk.Label(root, text="Escribe tu nombre:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Saludar", command=self.saludar)
        self.button.pack(pady=10)

        self.resultado = tk.Label(root, text="")
        self.resultado.pack()

    def saludar(self):
        nombre = self.entry.get() or "amigo"
        self.resultado.config(text=f"Hola, {nombre}!")


# Ejercicios sugeridos:
# 1. Crear una ventana con un botón que sume dos números.
# 2. Mostrar el valor de un checkbox en una etiqueta.
# 3. Crear un formulario con nombre, edad y botón de guardar.
# 4. Hacer una calculadora básica con Tkinter.

if __name__ == "__main__":
    root = tk.Tk()
    EjercicioApp(root)
    root.mainloop()
