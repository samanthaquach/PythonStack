from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST']) #to match with form /user change to /process
def create_user():
#    print request.form['name']
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   session['password'] = request.form['password']
   return redirect('/show') 

@app.route('/login', methods=['POST']) #can't have two /process
def login():
    if request.form['action'] == 'register':
        return redirect('/show')
    elif request.form['action'] == 'login':
        return redirect('/') 
    print request.form['email']
   
    session['email'] = request.form['email']
    session['password'] = request.form['password']

    return redirect('/show')




@app.route('/show')
def show_user():
  return render_template('show.html', name=session['name'])

app.run(debug=True) # run our server
