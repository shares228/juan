# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludar', methods=['POST'])
def saludar():
    nombre = request.form.get('nombre', '').strip()
    edad = request.form.get('edad', '').strip()

    if not nombre:
        mensaje = "Por favor, ingresa tu nombre."
    else:
        mensaje = f"Hola, {nombre}!"
        if edad.isdigit():
            edad_int = int(edad)
            if edad_int < 18:
                mensaje += f" Tienes {edad_int} años, eres menor de edad."
            else:
                mensaje += f" Tienes {edad_int} años, eres mayor de edad."

    return render_template('resultado.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
