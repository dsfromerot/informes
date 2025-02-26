from flask import Flask
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configuración de Flask y Keycloak
app.config.update({
    'SECRET_KEY': 'secret',
    'OIDC_CLIENT_SECRETS': '/app/client_secrets.json',  # Ruta absoluta
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)

# Importar rutas después de inicializar Flask para evitar errores de importación circular
from app import routes  

# Gunicorn busca esta función para iniciar Flask
def start():
    return app
