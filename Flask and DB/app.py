import requests

from flask import Flask, render_template, request, redirect
import psycopg2

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="R12hf3gFef7iu90o",
                        host="localhost",port="5432")
cursor = conn.cursor()
cursor.execute("SELECT login FROM service.users;")
print(cursor.fetchall())

app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')  

            cursor.execute("SELECT login FROM service.users;")
            logins = cursor.fetchall()
            registered = False
            for log in logins:
                if log[0] == username:
                    registered = True
            if not registered:    
                return redirect('/login_error/')

            password = request.form.get('password')
            cursor.execute("SELECT password FROM service.users WHERE login="+'\''+username+'\'')
            true_pass = cursor.fetchall()[0][0]
            if true_pass != password:
                return redirect('/login_error/')

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())

            return render_template('account.html', full_name=records[0][1])
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        registered = False
        cursor.execute("SELECT login FROM service.users;")
        logins = cursor.fetchall()
        for log in logins:
            if log[0] == str(login):
                registered = True
            
        if (len(str(name)) != 0 and len(str(login)) != 0 and len(str(password)) != 0) and not registered:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
            conn.commit()
        else:
            return redirect('/registration_error/')

        return redirect('/login/')

    return render_template('registration.html')

@app.route('/registration_error/', methods=['GET'])
def registration_error():
    return render_template('registration_error.html')

@app.route('/login_error/', methods = ['GET'])
def login_error():
    return render_template('login_error.html')
