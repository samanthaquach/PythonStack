from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

  return render_template('index.html')
  
@app.route('/process', methods=['Post'])
def process():
    if len(request.form['email']) < 1:
        # print ('retry')
        flash("Email cannot be empty! ")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!") 
    else:
        print('awesome')
    # ---------------------------------------
    if len(request.form['first_name']) < 1:
        flash("Name cannot be empty!")
    elif request.form['first_name'] != int:
        flash("Name cannot be contained with numbers!")
    else:
        print('awesome')
    # ---------------------------------------
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif request.form['last_name'] != int:
        flash("Last name cannot be contained with numbers!")
    else:
        print('awesome')
    # ---------------------------------------
    if len(request.form['password']) < 1:
        flash("Password cannot be empty!")
    elif request.form['password'] > 8:
        flash("Password has to be more than 8 characters!")
    else:
        print('awesome')
    # ----------------------------------------
    if request.form['confirm_password'] == request.form['password']:
        print ('match')
    else:
        flash("Password do not match!")
        
    return redirect('/')





app.run(debug=True) 