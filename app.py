#importar flask
#pip install flask
from flask import Flask, jsonify

#array que simula una BD y que Jsonify lo convierte en JSON para la respuesta
personas = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Mari"},
    {"id": 3, "nombre": "Pepe"},
]
#Flask
app = Flask(__name__)

#Ruta personas para obtener la lista de personas del array
@app.route("/personas", methods=["GET"])
def obtener_personas():
    return jsonify(personas)

#Ejecutar el servidor de flask en el puerto 5000 y debug para actualizar cambios
if __name__ == "__main__":
    app.run(debug=True, port=5000)
