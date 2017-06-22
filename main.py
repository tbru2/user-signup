from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    error_check = False
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if " " in username or username == '':
        username_error = "Not a proper username."
        error_check = True
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username is not the proper length."
        error_check = True
    if ' ' in password or password == '':
        password_error = "Not a proper password."
        password = ''
        verify_password = ''
        error_check = True
    if password != verify_password:
        verify_password_error = "Passwords don't match."
        password = ''
        verify_password = ''
        error_check = True
    if verify_password == '':
        verify_password_error = "Passwords don't match."
        error_check = True
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password is not the proper length."
        password = ''
        verify_password = ''
        error_check = True
    if email != '':
        if email.count('@') != 1:
            email_error = "Not a valid email address."
            error_check = True
        if email.count('.') != 1:
            email_error = "Not a valid email address."
            error_check = True
        if " " in email:
            email_error = "Not a valid email address."
            error_check = True
        if len(email) < 3 or len(email) > 20:
            email_error = "Not a valid email address."
            error_check = True
    if error_check == True:
        return render_template("index.html", username_error=username_error,
            password_error=password_error, verify_password_error=verify_password_error,
            email_error=email_error, username=username, password=password,
            verify_password=verify_password, email=email)
    else:
        return render_template("welcome.html", username = username)

app.run()