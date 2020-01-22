from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num_rows=int(9), num_cols=int(9))

@app.route('/<num>')
def checkerinputnum(num):
    return render_template('index.html', num_rows=int(num), num_cols=int(num))



@app.route('/<x>/<y>')
def checkerinputnumbers(x,y):
    return render_template('index.html', num_rows=int(x), num_cols=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def checkerinputnumbersandcolors(x,y,color1,color2):
    return render_template('index.html', num_rows=int(x), num_cols=int(y), colorx = color1, colory = color2)

if __name__ == '__main__':
    app.run(debug=True)
