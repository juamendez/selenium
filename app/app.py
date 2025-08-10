from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/login">
            <input type="text" name="username" id="username" />
            <input type="password" name="password" id="password" />
            <input type="submit" id="submit" />
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'user' and password == 'pass':
        return f'Bienvenido {username}'
    return 'Credenciales incorrectas', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
