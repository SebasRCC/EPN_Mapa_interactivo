from flask import Flask, request, jsonify, render_template
import json
import unicodedata
import os

app = Flask(__name__)

# Cargar datos de lugares
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "lugares_epn.json")

with open(json_path, "r", encoding="utf-8") as f:
    lugares = json.load(f)

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def buscar_lugar(pregunta):
    pregunta = quitar_tildes(pregunta.lower())
    for clave, datos in lugares.items():
        for alias in datos["alias"]:
            if alias in pregunta:
                return{
                    "nombre": datos["nombre"],
                    "ubicacion": datos["ubicacion"],
                    "lat": datos.get("lat", 0),
                    "lng": datos.get("lng", 0),
                }
    return None

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.get_json()
    pregunta = normalizar(data.get('pregunta', ''))

    for lugar in lugares:
        if isinstance(lugar, dict):  # ← seguridad extra
            for alias in lugar.get('alias', []):
                if normalizar(alias) in pregunta:
                    return jsonify(success=True, lugar=lugar)

    return jsonify(success=False, mensaje="Lo siento, no reconozco el lugar que mencionas. Intenta ser más específico.")


if __name__ == "__main__":
    app.run(debug=True)
