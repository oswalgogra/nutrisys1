from app import app
from flask import request, session, abort, redirect, url_for
from controller.control import Control

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    controlador = Control()
    return controlador.index_page()

@app.route('/services')
def services():
    controlador = Control()
    return controlador.services_page()

@app.route('/contact')
def contact():
    controlador = Control()
    return controlador.contact_page()

@app.route('/form-login')
def form_login():
    controlador = Control()
    return controlador.render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    controlador = Control()
    if 'user' in session:
        return redirect(url_for('/schedule'))
    else:
        session['user'] = request.form['username']
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    controlador = Control()
    session.pop('user', None)
    session.pop('citas', None)
    return controlador.index_page()

@app.route('/schedule')
def schedule():
    controlador = Control()
    return controlador.schedule_page()

@app.route('/save-schedule', methods=['GET','POST'])
def save_schedule():
    controlador = Control()
    datosRecibidos = request.form
    print(datosRecibidos)
    nombre = datosRecibidos['nombre']
    email = datosRecibidos['email']
    telefono = datosRecibidos['telefono']
    especialidad = datosRecibidos['especialidad']
    fecha = datosRecibidos['fecha']
    sintomas = datosRecibidos['sintomas']
    result = controlador.insert_schedule(cita={'nombre': nombre, 'email': email, 'telefono': telefono, 'especialidad': especialidad, 'fecha': fecha, 'sintomas': sintomas})
    if result == True:
        return "Los datos fueron guardados exitosamente!"
    return False

@app.route('/schedules')
def schedules():
    controlador = Control()
    return controlador.schedules_page()

