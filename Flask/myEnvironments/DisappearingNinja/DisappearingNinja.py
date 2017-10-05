from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def tmnt():
	return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninja_color(color):
    if (color == "blue"):
        return render_template('leonardo.html')
    elif (color == "orange"):
        return render_template('Michaelangelo.html')
    elif (color == "red"):
        return render_template('rafael.html')
    elif (color == "purple"):
        return render_template('donatello.html')
    else:
        return render_template('notapril.html')



# @app.route('/blue')
# def leo():
# 	return render_template('leonardo.html')

# @app.route('/red')
# def rafael():
# 	return render_template('rafael.html')

# @app.route('/orange')
# def michael():
# 	return render_template('Michaelangelo.html')

# @app.route('/purple')
# def donatello():
# 	return render_template('donatello.html')

# @app.route('/123')
# def notapril():
# 	return render_template('notapril.html')


         
app.run(debug=True)