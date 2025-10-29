from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/formulario')
def formulario():
    if request.method == 'POST':
        Peso = request.form.get('Peso')
        Altura = request.form.get('Altura')
        Edad = request.form.get('Edad')
        genero = request.form.get('genero')


        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{Peso},{Altura},{Edad},{genero}\n")
        return redirect(url_for('inicio'))
    return render_template('formulario.html')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
