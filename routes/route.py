from app import app
from flask import request, session, abort, redirect, url_for
from controller.control import *

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return index_page()

@app.route('/services')
def services():
    return services_page()

@app.route('/contact')
def contact():
    return contact_page()

@app.route('/form-login')
def form_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if 'user' in session:
        return redirect(url_for('/schedule'))
    else:
        session['user'] = request.form['username']
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('citas', None)
    return index_page()

@app.route('/appointments')
def appointments():
    return render_template('appointments.html')

@app.route('/schedule')
def schedule():
    return schedule_page()

@app.route('/save-schedule', methods=['GET','POST'])
def saveSchedule():
    print("******** datos recibidos: ***********")
    datosRecibidos = request.form
    print(datosRecibidos)
    print("***** fin datos recibidos **** ")

    nombre = datosRecibidos['nombre']
    email = datosRecibidos['email']
    telefono = datosRecibidos['telefono']
    especialidad = datosRecibidos['especialidad']
    fecha = datosRecibidos['fecha']
    sintomas = datosRecibidos['sintomas']
    insert_cita(cita={'nombre': nombre, 'email': email, 'telefono': telefono, 'especialidad': especialidad, 'fecha': fecha, 'sintomas': sintomas})
    return "Los datos fueron guardados exitosamente!"

@app.route('/schedules')
def schedules():
    session
    return schedules_page(session.get('citas'))

def insert_cita(cita):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO cita (paciente, especialidad, fecha, email, telefono, sintomas) VALUES ",
                    "('%s','%s','%s','%s','%s','%s')",(cita['nombre'],cita['especialidad'],cita['fecha'],
                    cita['email'],cita['telefono'],cita['sintomas']))
    mysql.connection.commit()
    cursor.close()
    return True
