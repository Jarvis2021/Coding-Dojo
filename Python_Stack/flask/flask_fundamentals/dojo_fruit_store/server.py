from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    results_redirected = request.form
    Customer = results_redirected['first_name'] + "," + results_redirected['last_name']
    fruit_count = int(results_redirected['strawberry']) + int (results_redirected['raspberry']) + int(results_redirected['apple'])
    print (f"Charging {Customer} for {fruit_count} fruits.")
    return render_template("checkout.html", results_redirected = request.form)

@app.route('/fruits')
def fruits():
    print(request.form)
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
