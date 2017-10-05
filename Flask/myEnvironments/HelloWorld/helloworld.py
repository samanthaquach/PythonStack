from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/show_me_sam') #copy and paste app.route/Try naming the route and title consistent
def Show_Sam():
	return '<p1>Here is Sam!</p>', {'Content-Type': 'text/html'}

@app.route('/<greeting>/<person>') #copy and paste app.route/Try naming the route and title consistent
def greet_person(greeting, person):
	return greeting + " " + person




app.run(debug=True)
