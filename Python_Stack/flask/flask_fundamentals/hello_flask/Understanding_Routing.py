from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<userinput>')
def hellodojo(userinput):
    return userinput.title()

@app.route('/say/<userinput>')
def helloinput(userinput):
    return "Hi " + userinput.title() + "!"

@app.route('/repeat/<num>/<userinput>')
def hellorepeat(num,userinput):
    return int(num) * userinput + "*"



if __name__=="__main__":
    app.run(debug=True)
