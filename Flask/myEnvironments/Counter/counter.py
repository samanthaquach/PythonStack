from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def run():
    if session.has_key('count') == False:
        session['count'] += 0
    else: 
        session['count'] += 1

    return render_template('index.html')

@app.route('/add', methods=['POST'])
def button_add():
    if session.has_key('count') == False:
        session['count'] = 0
    else:
        session['count'] += 1
    
    return redirect('/')



@app.route('/refresh', methods=['POST'])
def button_refresh():
    session['count'] = -1
    
    return redirect('/')


@app.route('/counter')
def show_user():
    return render_template('counter.html')



app.run(debug=True)