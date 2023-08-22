from flask import render_template, session

def index_page():
    return render_template('index.html')

def services_page():
    return render_template('services.html')

def contact_page():
    return render_template('contact.html')

def schedule_page():
    return render_template('schedule.html')

def save_schedule():
    return 'Schedule created successfully!'

def schedules_page(citas):
    if 'user' not in session.keys():
        session['citas'] = ()
    return render_template('schedules_list.html', schedules=citas)

def cargar_citas():
    session['citas'] = [
        {'nombre': 'Oswaldo', 'fecha': '24-08-2023', 'especialidad': 'Nutrición'},
        {'nombre': 'Adriana', 'fecha': '24-08-2023', 'especialidad': 'Nutrición'},
        {'nombre': 'Luz', 'fecha': '25-08-2023', 'especialidad': 'Fisioterapia'},
        {'nombre': 'Cesar', 'fecha': '26-08-2023', 'especialidad': 'Medicina general'}]

def get_citas():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM cita""")
    rv = cur.fetchall()
    return str(rv)