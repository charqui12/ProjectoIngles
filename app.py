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

@app.route("/juegos")
def juegos():
    return render_template("juegos.html")

if __name__ == "__main__":
    app.run(debug=True)
