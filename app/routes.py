from flask import jsonify
from app.config import app, oidc
# Datos hardcodeados
informes = [
    {"nombre_doctor": "Dr. Smith", "vida_o_muerte": "Vida", "descripcion": "Paciente estable"},
    {"nombre_doctor": "Dr. Johnson", "vida_o_muerte": "Muerte", "descripcion": "Paciente fallecido"}
]

@app.route('/informe', methods=['GET'])
@oidc.accept_token(True)
def get_informe():
    return jsonify(informes)
