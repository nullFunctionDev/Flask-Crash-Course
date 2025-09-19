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

# We can also make a page that returns something simple
@app.route("/simple")
def simple():
    return 'This is a simple message'

# Run the app in debug mode to see live updates/info in terminal
if __name__ == '__main__':
    app.run(debug=True)