from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def about_ninjas():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def hello_dojo():
    return render_template('dojos.html')


app.run(debug=True)