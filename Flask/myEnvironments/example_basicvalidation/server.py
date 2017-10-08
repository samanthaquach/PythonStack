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
  #do some validations here!
#   if len(request.form['name']) < 1:
  if len(request.form['email']) < 1:  
    #   print('oh no')
    # flash("Name cannot be empty!")
        flash("Email cannot be blank!")
    # else if email doesn't match regular expression display an "invalid email address" message
    # display validation errors
  elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")  
  else:
    #   print('yes')
    #   flash("Success! Your name is {}".format(request.form['name'])) 
        flash("Success!")
    # display success message
  return redirect('/') # either way the application should return to the index and display the message
app.run(debug=True)
