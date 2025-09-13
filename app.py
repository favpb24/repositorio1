from flask import Flask, render_template
import random

app = Flask(__name__)

datos_curiosos = [
    "Las abejas pueden reconocer rostros humanos.",
    "Un pulpo tiene tres corazones.",
    "Los delfines duermen con un ojo abierto.",
    "La miel nunca se echa a perder.",
    "Los flamencos son blancos al nacer.",
    "Los astronautas pueden crecer hasta 5 cm en el espacio.",
    "El tiburón ballena es el pez más grande del mundo.",
    "Las mariposas saborean con sus patas.",
    "Una nube puede pesar más de 500 mil kilos.",
    "Los camellos tienen tres párpados para protegerse de la arena."
]

@app.route("/")
def inicio():
    curiosidad = random.choice(datos_curiosos)
    return render_template("index.html", curiosidad=curiosidad)

if __name__ == "__main__":
    app.run(debug=True)
