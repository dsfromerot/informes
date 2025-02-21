from flask import Flask, jsonify

app = Flask(__name__)

informes = [
    {"nombre_doctor": "Dr. Smith", "vida_o_muerte": "Vida", "descripcion": "Paciente estable"},
    {"nombre_doctor": "Dr. Johnson", "vida_o_muerte": "Muerte", "descripcion": "Paciente fallecido"}
]

@app.route('/informes', methods=['GET'])
def get_informes():
    return jsonify(informes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
