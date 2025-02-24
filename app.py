from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)

# Configura Keycloak
oauth.register(
    name='keycloak',
    client_id='informes',  # Cambia el client_id para este microservicio
    client_secret='JVXLreXPsPldkoR1ZmVswqgW0zwiHXHq',  # Cambia el client_secret
    authorize_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/auth',
    authorize_params=None,
    access_token_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://100.93.128.110:5003/callback',  # Cambia el puerto
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/informes', methods=['GET'])
def get_informes():
    token = oauth.keycloak.authorize_access_token()
    if not token:
        return jsonify({"error": "Acceso no autorizado"}), 401
    informes = [
        {"nombre_doctor": "Dr. Smith", "vida_o_muerte": "Vida", "descripcion": "Paciente estable"},
        {"nombre_doctor": "Dr. Johnson", "vida_o_muerte": "Muerte", "descripcion": "Paciente fallecido"}
    ]
    return jsonify(informes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)  # Cambia el puerto
