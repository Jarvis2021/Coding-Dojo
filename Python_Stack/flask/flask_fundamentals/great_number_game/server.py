from flask import Flask, session, request, render_template, redirect
from random import randint

app = Flask(__name__)
app.secret_key="b'g\xa2\xb8M\xad\xc0t\xc8doX\xfe\r\x96\xd7\xba'"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    session['user_input'] = request.form['userinput']
    print(f"User Input is: {session['user_input']}")
    session['rand_num'] = randint(1,100)
    print(f"Random Number Generated: {session['rand_num']} ")
    if int(session['user_input']) < int(session['rand_num']):
         message_low = "Too Low!"
    elif int(session['user_input']) > int(session['rand_num']):
         message_high = "Too High!"
    else:
        pass

    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)
