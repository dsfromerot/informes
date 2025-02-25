from flask import Flask
from flask_oidc import OpenIDConnect

app = Flask(__name__)
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

# Ruta de prueba
@app.route('/')
def hello():
    return "¡El microservicio de informes está en ejecución!"

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
