from flask import Flask, render_template, redirect, url_for, request, jsonify
from login import login 
from sensors import sensor_blueprint
from actuator import actuator_blueprint
app = Flask(__name__)

users = {
    'user1': '1234',
    'leonadro': 'min'
}
sensores = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
atuadores = {'Servo':122, 'Lâmpada':1}

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor_blueprint, url_prefix='/')
app.register_blueprint(actuator_blueprint, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/demonstration', methods=['GET'])
def demonstration():
    return jsonify(sensores)

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')
    

# ============================== USER ==============================
@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_users():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", devices=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)

@app.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", devices=users)

@app.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        users.pop(user)
    else:
        user = request.args.get('user', None)
        if user:
            users.pop(user)
    return render_template("users.html", devices=users)
# ============================== SENSOR ==============================
@app.route('/sensors')
def sensors():
    return render_template('sensors.html', devices=sensores)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global users
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor']
    else:
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
    sensores[sensor] = valor
    return render_template("sensors.html", devices=sensores)

@app.route('/remove_sensor')
def remove_sensors():
    return render_template("remove_sensor.html", devices=sensores)

@app.route('/del_sensor', methods=['GET','POST'])
def del_sensors():
    global sensores
    if request.method == 'POST':
        sensor_to_remove = request.form['sensor']
        sensores.pop(sensor_to_remove, None)  
    else:
        sensor_to_remove = request.args.get('sensor', None)
        if sensor_to_remove in sensores:
            sensores.pop(sensor_to_remove, None) 
    return render_template("sensors.html", devices=sensores)

# ============================== ACTUADOR ==============================
@app.route('/actuators')
def actuators():
    return render_template('actuators.html', devices=atuadores)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global users
    if request.method == 'POST':
        atuador = request.form['atuador']
        valor = request.form['valora']
    else:
        atuador = request.args.get('atuador', None)
        valor = request.args.get('valora', None)
    atuadores[atuador] = valor
    return render_template("actuators.html", devices=atuadores)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=atuadores)

@app.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        actuator_to_remove = request.form['actuators']  # Corrigindo para 'actuators'
        atuadores.pop(actuator_to_remove, None)  
    else:
        actuator_to_remove = request.args.get('actuators', None)  # Corrigindo para 'actuators'
        if actuator_to_remove in atuadores:
            atuadores.pop(actuator_to_remove, None) 
    return render_template("actuators.html", devices=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)