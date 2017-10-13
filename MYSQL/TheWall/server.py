from flask import Flask, render_template, request, redirect, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
import datetime
import time
import os, binascii

app = Flask(__name__)
mysql = MySQLConnector(app, 'TheWall')

print mysql.query_db("SELECT * FROM users")

app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    created_at = time.strftime('%m-%d-%Y')
    users = mysql.query_db("SELECT * FROM users")
    messages = mysql.query_db("SELECT * FROM messages")  
    post_messages = mysql.query_db("select users.first_name, messages.message, concat( monthname(messages.created_at), ' ', Day(messages.created_at)) AS message_date, year(messages.created_at) AS year_name from users JOIN messages ON users.id = messages.users_id ORDER BY messages.created_at DESC")

    return render_template('index.html', users=users, messages=messages, post_messages=post_messages)

@app.route('/process', methods=['POST'])
def process():

    return redirect('/')

# WALL ----------------------------------------
@app.route('/TOTheWall', methods=['GET'])
def TO_TheWall():
    created_at = time.strftime('%m-%d-%Y')
    users = mysql.query_db("SELECT * FROM users")
    messages = mysql.query_db("SELECT * FROM messages")  
    post_messages = mysql.query_db("select users.first_name, messages.id, messages.message, concat( monthname(messages.created_at), ' ', Day(messages.created_at)) AS message_date, year(messages.created_at) AS year_name from users JOIN messages ON users.id = messages.users_id ORDER BY messages.created_at DESC")
    post_comments = mysql.query_db("SELECT users.first_name AS name, messages.id AS message_id, messages.message, comments.id, comments.comment AS comment, concat( monthname(comments.created_at), ' ', Day(comments.created_at)) AS comment_date, year(comments.created_at) AS year_name, comments.users_id AS user_id from messages JOIN comments ON messages.id=comments.messages_id JOIN users ON comments.users_id=users.id")

    print post_comments

    
    return render_template('wall.html', users=users, messages=messages, post_messages=post_messages, post_comments=post_comments)

@app.route('/post_comments', methods=['POST'])
def post_comments():
    message_id=request.form['message_id']
    id = session['id'] 
    
    comment = request.form['text_area']

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    mysql.query_db ("INSERT INTO comments (messages_id, updated_at, users_id, comment, created_at) VALUES ('{}','{}','{}','{}','{}')".format (message_id, updated_at, id, comment, created_at))

    flash ('You have been successfully submitted your comments!')

    return redirect('/TOTheWall')


# register ------------------------------------
@app.route('/register', methods=['GET'])
def register():
 
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    errors = []
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # password = md5.new(request.form['password']).hexdigest()
    salt = binascii.b2a_hex(os.urandom(15))
    password = md5.new(request.form['password'] + salt).hexdigest()


    existingEmails = mysql.query_db("SELECT * FROM users WHERE email = '{}' ".format(email) ) 

    if len(request.form['email']) < 1:
        errors.append("Email cannot be empty!")

    if len(existingEmails) > 0:
        flash("Email Already Exists! Try logging in!")
        return redirect('/login')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")

    # ----------------------------------------------
    if len(request.form['first_name']) < 1:
        errors.append("First Name cannot be empty!")

    if not NAME_REGEX.match(first_name):
        errors.append("First Name Cannot Contain Any Numbers!")

    # ---------------------------------------
    if len(request.form['last_name']) < 1:
        errors.append("Last Name cannot be empty!")

    if not NAME_REGEX.match(last_name):
        errors.append("Last Name Cannot Contain Any Numbers!")

    # ---------------------------------------
    if len(request.form['password']) < 1:
        errors.append("password cannot be empty!")

    if request.form['password'] < 3:
        errors.append("Password has to be more than 3 characters!")

    # ----------------------------------------
    if request.form['confirm_password'] == request.form['password']:
        print ('match')
    else:
        errors.append("Password do not match!")
    # ----------------------------------------
    if len(errors) > 0:
        flash(errors)

    else:
        mysql.query_db ("INSERT INTO users (email, first_name, last_name, password, salt) VALUES ('{}','{}','{}','{}','{}')".format(email,first_name,last_name,password, salt))
        flash ('You have been successfully registered! Now, log in.')
        return redirect('/')

    return redirect('/')

# log in ------------------------------------

@app.route('/GetToLogin', methods=['GET'])
def Get_Login():
 
    return render_template('login.html')

@app.route('/PrimaryLogin', methods=['POST'])
def Primary_Login():
    email = request.form['email']
    password = request.form['password']
    users = mysql.query_db("SELECT * FROM users WHERE email = '{}' ".format(email) ) 
    if len(users) > 0:
        user = users[0]
        
        new_salt = str(user['salt'])
        encrypted_password = md5.new(password + new_salt).hexdigest()

        if user['password'] == encrypted_password:
            session['first_name'] = user['first_name']
            session['id'] = user['id']
            flash('Yay, you are logged in')
            return redirect('/')
        #Needed two else statements?
        else:
            print "Password Invalid"
            flash('Password Invalid')
    else:
        print "no such user"
        flash('No Such User!')

    return redirect('/GetToLogin')

# log out --------------------------------------
    
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

# post message -----------------------------------

@app.route('/post_message', methods=['POST'])
def post_message():
    id = session['id']
    message = request.form['text_area']
    created_at = datetime.datetime.now()
    mysql.query_db ("INSERT INTO messages (users_id, message, created_at) VALUES ('{}','{}','{}')".format (id, message, created_at))
    print message

    flash ('You have been successfully submitted your message!')

    return redirect('/')
    

app.run(debug=True)