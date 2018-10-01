from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def display_user_signup_form():
    return render_template("main.html")

def empty_value(x):
    if x: 
        return True
    else:
        return False

def length_of_char(x):
    if len(x) < 21 and len(x) > 2:
        return True
    else:
        return False

def at_symbol(x):
    if x.count("@") >= 1:
        return True
    else:
        return False

def more_than_one_at(x):
    if x.count("@") <= 1:
        return True
    else:
        return False
def email_dot(x):
    if x.count(".") >= 1:
        return True
    else:
        return False


def more_than_one_dot(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

@app.route("/", methods = ["POST"])
def signup_complete():
    username = request.form["username"]
    password = request.form["password"]
    password_validate = request.form["password_validate"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "must not contain spaces"

    if not empty_value(password):
        password_error = err_required
        password = ''
        password_validate = ''
    elif not length_of_char(password):
        password_error = "Password " + err_char_count
        password = ''
        password_validate = ''
        password_validate_error = err_reenter_pw
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            password_validate = ''
            password_validate_error = err_reenter_pw

    if not empty_value(username):
        username_error = err_required
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    elif not length_of_char(username):
        username_error = "Username " + err_char_count
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw

    if empty_value(email):
        if not length_of_char(email):
            email_error = "Email " + err_char_count
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not more_than_one_at(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not email_dot(email):
            email_error = "Email must contain ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not more_than_one_at(email):
            email_error = "Email must contain only one ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        else:
            if " " in email:
                email_error = "Email " + err_no_spaces
                password = ''
                password_validate = ''
                password_error = err_reenter_pw
                password_validate_error = err_reenter_pw

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)


@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()
