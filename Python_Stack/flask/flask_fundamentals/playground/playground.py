from flask import Flask,render_template
app = Flask(__name__)


@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def playground():
    return render_template("index.html",times=3)

@app.route('/play/<num>')          # The "@" decorator associates this route with the function immediately following
def play(num):
    return render_template("index.html", times=int(num))

@app.route('/play/<num>/<color>')          # The "@" decorator associates this route with the function immediately following
def playcolor(num,color):
    return render_template("index.html",times=int(num), boxcolor =color)



if __name__=="__main__":
        app.run(debug=True)
