from flask import Flask, render_template, request, redirect, session
import random



app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def run():
    session['givenNum'] = random.randrange(0,100)
    return render_template('index.html')

@app.route('/process', methods=['POST']) 
def guess_process():
    session['playNumber'] = int(request.form['playNumber'])
    print request.form['playNumber']
    print session['givenNum']
    if session['playNumber'] < session['givenNum']:
        session['guessAnswer'] = 'low'
        print session['guessAnswer']
        session['guess_status'] = 'show_div'
        return redirect('/')
    if session['playNumber'] > session['givenNum']:
        session['guessAnswer'] = 'high'
        print session['guessAnswer']
        session['guess_status'] = 'show_div'
        return redirect('/')
    elif session['playNumber'] == session['givenNum']:
        print('yay')
        session['guessAnswer'] = 'correct'
        return redirect('/yay')
    session.pop('playNumber')


@app.route('/restart', methods=['POST'])
def answer():
    session['guess_status'] = 'hide_div'
    return redirect('/')

@app.route('/yay')
def yay():
    return render_template('yay.html', playNumber=session['playNumber'])

app.run(debug=True)

