from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM email")

app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    errors = []
    email = request.form['email']
    existingEmails = mysql.query_db("SELECT * FROM email WHERE address = '{}' ".format(email) ) 
    if len(request.form['email']) < 1:
        errors.append("Email cannot be empty!")
        # flash("Email cannot be empty! ")
    if len(existingEmails) > 0:
        errors.append("Email Already Exists!")
        # flash("Email Already Exists!")
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")
    if len(errors) > 0:
        flash(errors)
    else:
        flash("Success!") 
        # created_at = datetime.datetime.now()
        mysql.query_db ("INSERT INTO email (address) VALUES ('{}')".format(email))
        return redirect('/success')
        print email

    return redirect('/')

@app.route('/success')
def successPage():
    print mysql.query_db("SELECT * FROM email") 
    email = mysql.query_db("SELECT * FROM email") 

    return render_template('success.html', email=email)

# @app.route('/refresh', methods=['POST'])
# def clear_refresh():
#     query = "delete from friends"
#     mysql.query_db(query)
    
#     return redirect('/')
app.run(debug=True)