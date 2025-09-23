# Flask app
from flask import Flask, render_template

# Init app
app = Flask(__name__)

name = "nullFunctionDev"
age = 99
student = False

# Home page, landing, default
@app.route('/')
def home():
    return render_template("home.html", person=name, age=age, student=student)

'''Other methods:
Return a string to the webpage
@app.route('/')
def home():
    return "nullFunctionDev()'s first video!"

Return a static HTML page
@app.route('/')
def home():
    return render_template("home.html")
'''

# Run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)