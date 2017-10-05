from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['POST'])
def create_user():
   print request.form['name']
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/show/' + name)

@app.route('/show/<name>')
def submitSuccess(name):
   print name
	 # Here's the line that changed. We're rendering a template from a post route now.
   return render_template('show.html', name=name)


app.run(debug=True) # run our server
