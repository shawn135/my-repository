# Using Jinja templates

# Import Flask and render_template modules.
from flask import Flask, render_template

# Create an object named app from imported Flask module.
app = Flask(__name__)

# Create a function named head which sends number number1 and number2 
# variables to the index.html. Use these variables into the index.html file. 
# Assign a URL route the head function with decorator @app.route('/').
@app.route("/")
def head():
    return render_template("index.html", number1=10, number2=20)



# send dynamic variables to the inde.html file
app.route("/number/<string:num1>/<string:num2>")
def custom(num1, num2):
    return render_template("index.html:", number1=num1, number2=num2)


# Create a function named number which sends number num1 and num2 and sum of them to 
# the body.html. Assign a URL route the number function with decorator @app.route('/sum').
@app.route("/sum/<string:a>/<string:b>")
def number(a, b):
    if a.isdigit() and b.isdigit():
        total = int(a) + int(b)
        html_code = render_template("body.html", num1=a, num2=b, sum=total)
        return html_code
    else:
        return "Invalid numbers to add together"




app.run(debug=False)