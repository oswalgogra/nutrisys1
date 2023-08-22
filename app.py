from flask import Flask, render_template, session
from flask_mysqldb import MySQL

app = Flask(__name__)
# Parámetros de conexión a la bd
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "nutrisys"
mysql = MySQL(app)

from routes.route import *

if __name__ == '__main__':
    app.run(debug=True)