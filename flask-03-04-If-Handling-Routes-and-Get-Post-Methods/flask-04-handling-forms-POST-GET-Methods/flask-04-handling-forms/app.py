# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)

# Create welcome page with main.html file and assigning it to the root path
@app.route("/")
def home():
    return render_template("main.html", name = "Shawn")




# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised
@app.route('/greet')
def greet():
    if 'user' in request.args:
        usr = request.args['user']
        return render_template("greet.html", user = usr)
    else: 
        return render_template("greet.html", user = "please add you ruser name to the query string")





# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("username")
        pw = request.form.get("password")
        if user_name == "clarusway" and pw == "clarusway":
            return render_template("secure.html", user = user_name)
        else: 
            return render_template("login.html", user=user_name, control = True)
    else:
        return render_template("login.html", control=True)




# Add a statement to run the Flask application which can be reached from any host.
if __name__ == '__main__':
    app.run("0.0.0.0")