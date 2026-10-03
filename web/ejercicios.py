"""Ejercicios didácticos para la carpeta web.

Objetivo: practicar HTML, CSS y JavaScript básicos para desarrollar
interfaces web sencillas.
"""


def ejercicio_1_html_basico():
    return """
    <h1>Hola Mundo</h1>
    <p>Este es un ejercicio básico de HTML.</p>
    """


def ejercicio_2_js_suma():
    return """
    let a = 5;
    let b = 7;
    console.log(a + b);
    """


def ejercicio_3_formulario():
    return """
    <form>
      <input type="text" placeholder="Nombre">
      <button type="submit">Enviar</button>
    </form>
    """


def ejercicio_4_css_card():
    return """
    .card {
      background: #f4f4f4;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    """


if __name__ == "__main__":
    print("Ejercicio HTML:")
    print(ejercicio_1_html_basico())
    print("\nEjercicio JS:")
    print(ejercicio_2_js_suma())
    print("\nEjercicio formulario:")
    print(ejercicio_3_formulario())
