# Importing Flask
from flask import Flask, render_template

# Initialize the app
app = Flask(__name__)

# Store our name variable to pass it to the html file
name = "nullFunctionDev()"

# Making the Home Page
@app.route('/')
def home():
    return render_template("home.html", person=name)

# Another page with some elements on it
@app.route('/another')
def another():
    return render_template("another.html")

# Run the app in debug mode to see live updates/info in terminal
if __name__ == '__main__':
    app.run(debug=True)