import re
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

username = ""
password = ""

@app.route('/success/<name>')
def success(name):
    return f'congratulations {name}, you have successfully logged in!'

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        uNameAttempt = request.form['name']
        pWdAttempt = request.form['password']
        return redirect(url_for('success', name=username)) if check_login_information(uNameAttempt, pWdAttempt) else  f'Sorry {username} that does not count!'
    return render_template('authentication/login.html')

def check_login_information(name, passw):
    return name == username and passw == password

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        return redirect(url_for('login'))
    return render_template('authentication/register.html')

if __name__ == "__main__":
    app.run(debug=True)