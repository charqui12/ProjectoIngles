from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vocabulario")
def vocabulario():
    return render_template("bocabulario.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")
@app.route("/comidas")
def comidas():
    return render_template("comidas.html")
@app.route("/ropa")
def ropa():
    return render_template("ropa.html")
@app.route("/colores")
def colores():
    return render_template("colores.html")

@app.route("/juegos")
def juegos():
    return render_template("juegos.html")
@app.route("/memorama")
def memorama():
    return render_template("memorama.html")

if __name__ == "__main__":
    app.run(debug=True)
