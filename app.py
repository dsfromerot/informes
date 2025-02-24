from flask import Flask, jsonify
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configuración de Keycloak
app.config.update({
    'SECRET_KEY': 'secret',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})
oidc = OpenIDConnect(app)

# Datos hardcodeados
informes = [
    {"nombre_doctor": "Dr. Smith", "vida_o_muerte": "Vida", "descripcion": "Paciente estable"},
    {"nombre_doctor": "Dr. Johnson", "vida_o_muerte": "Muerte", "descripcion": "Paciente fallecido"}
]

@app.route('/informe', methods=['GET'])
@oidc.accept_token(True)  # Protege la ruta con Keycloak
def get_informe():
    return jsonify(informes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
