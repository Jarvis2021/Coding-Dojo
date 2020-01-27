from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = "b'\x9e[3\xcf~W\xc7\x87\x8fF\xcdS\xf6\x11\xb4\x18'"

@app.route('/')
def landing():
    if "visits" not in session:
        session['visits'] = 1
    else:
        session['visits'] = session['visits'] + 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

@app.route('/doublevisits')
def addtwovisits():
    session['visits'] = session['visits'] + 1
    return redirect("/")

@app.route('/reset')
def reset_session():
    session.clear()
    return redirect("/")

@app.route('/incrementcounter', methods = ['POST'])
def incrementcounter():
    print(request.form)
    # session['visits'] = session['visits'] + {{request.form['countervalue']}}
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
