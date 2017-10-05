from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/projects') #copy and paste app.route/Try naming the route and title consistent
def projects():
	return render_template('projects.html')

@app.route('/about') #copy and paste app.route/Try naming the route and title consistent
def about_me():
	return render_template('aboutme.html')




app.run(debug=True)