from flask import render_template, session
from app import mysql

class Control():

    def __init__(self, nombre=''):
        self.nombre = nombre

    def index_page(self):
        return render_template('index.html')

    def services_page(self):
        return render_template('services.html')

    def contact_page(self):
        return render_template('contact.html')

    def schedule_page(self):
        return render_template('schedule.html')

    def insert_schedule(self, cita):
        cursor = mysql.connection.cursor()
        try:
            query = f"INSERT INTOD citax (paciente, especialidad, fecha, email, telefono, sintomas) VALUES ('{cita['nombre']}','{cita['especialidad']}','{cita['fecha']}','{cita['email']}','{cita['telefono']}','{cita['sintomas']}')"
            cursor.execute(query)
            mysql.connection.commit()
            cursor.close()
        except Exception:
            print(f"Error al ejecutar la sentencia: {query}")
            return False
        return True

    def schedules_page(self):
        citas = self.get_citas()
        for c in citas:
            print(c)
        return render_template('schedules_list.html', schedules=citas)

    def cargar_citas(self):
        session['citas'] = [
            {'nombre': 'Oswaldo', 'fecha': '24-08-2023', 'especialidad': 'Nutrición'},
            {'nombre': 'Adriana', 'fecha': '24-08-2023', 'especialidad': 'Nutrición'},
            {'nombre': 'Luz', 'fecha': '25-08-2023', 'especialidad': 'Fisioterapia'},
            {'nombre': 'Cesar', 'fecha': '26-08-2023', 'especialidad': 'Medicina general'}]

    def get_citas(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cita")
        rv = cur.fetchall()
        return rv