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
    if len(request.form['name']) < 1:
        # print ('retry')
        flash(" Name cannot be empty! ")
    else:
        print('awesome')
    if len(request.form['comment']) > 120:
        print ('awesome commenting')
    elif len(request.form['comment']) < 0:
        flash("Comment cannot be empty!")
    else:
        print('retry commenting')
        
    return redirect('/')



app.run(debug=True)