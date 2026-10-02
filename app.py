import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    env = os.environ.get('APP_ENV', 'unknown')
    db_user = os.environ.get('DB_USERNAME', 'none')
    return f"¡Hola Mundo desde Kubernetes! [Entorno: {env} | DB User: {db_user}]\n"

@app.route('/healthz')
def healthz():
    return jsonify(status="healthy"), 200

if __name__ == '__main__':
    # Debug desactivado para mitigar vulnerabilidad RCE en entornos de ejecución
    app.run(debug=False, host='0.0.0.0', port=5000)
