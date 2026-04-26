from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    if usuario == "admin" and clave == "1234":
        return f"<h1>Bienvenido, {usuario}</h1><p>Acceso correcto.</p>"
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

@app.route("/predict/<float:celsius>", methods=["GET"])
def predict_get(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32

    return jsonify({
        "celsius": celsius,
        "fahrenheit": fahrenheit
    })


if __name__ == "__main__":
    app.run(debug=True)