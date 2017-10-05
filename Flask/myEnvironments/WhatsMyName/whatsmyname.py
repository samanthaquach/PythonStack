from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
   print request.form['name']   
   
   name = request.form['name']
   email = request.form['email']
   return redirect('/show/' + name)

@app.route('/show/<name>')
def submitSuccess(name):
   print name
   return render_template('show.html', name=name)


app.run(debug=True)