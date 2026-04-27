from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 HABILITA CORS para Flutter

@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    if usuario == "admin" and clave == "1234":
        return f"""
        <h1>Bienvenido, {usuario}</h1>
        <p>Acceso correcto.</p>
        <a href="/convertidor">Ir al convertidor</a>
        """
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

@app.route("/predict/<float:celsius>", methods=["GET"])
def predict_get(celsius):
    fahrenheit = (celsius * 9/5) + 32

    return jsonify({
        "celsius": celsius,
        "fahrenheit": fahrenheit
    })

@app.route("/convertidor")
def convertidor():
    return render_template("convertidor.html", resultado=None)

@app.route("/convertir", methods=["POST"])
def convertir():
    celsius = float(request.form.get("celsius"))
    fahrenheit = (celsius * 9/5) + 32

    return render_template("convertidor.html", resultado=fahrenheit)

if __name__ == "__main__":
    app.run(debug=True)