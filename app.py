from flask import Flask, jsonify, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management
oauth = OAuth(app)

# Configure Keycloak
oauth.register(
    name='keycloak',
    client_id='informes',
    client_secret='JVXLreXPsPldkoR1ZmVswqgW0zwiHXHq',
    authorize_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/auth',
    access_token_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/token',
    redirect_uri='http://100.93.128.110:5003/callback',
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/login')
def login():
    # Redirect the user to Keycloak for authentication
    redirect_uri = url_for('callback', _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)

@app.route('/callback')
def callback():
    try:
        # Exchange the authorization code for an access token
        token = oauth.keycloak.authorize_access_token()
        if not token:
            return jsonify({"error": "Error en la autenticación"}), 401
        
        # Store the token in the session
        session['token'] = token
        return redirect(url_for('get_informes'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/informes', methods=['GET'])
def get_informes():
    # Check if the user is authenticated by verifying the token in the session
    token = session.get('token')
    if not token:
        return jsonify({"error": "Acceso no autorizado"}), 401
    
    # Return protected data
    informes = [
        {"nombre_doctor": "Dr. Smith", "vida_o_muerte": "Vida", "descripcion": "Paciente estable"},
        {"nombre_doctor": "Dr. Johnson", "vida_o_muerte": "Muerte", "descripcion": "Paciente fallecido"}
    ]
    return jsonify(informes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
