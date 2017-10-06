from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST']) #to match with form /user change to /process
def create_user():
   print request.form['name']
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])

app.run(debug=True) # run our server
