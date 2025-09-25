# Flask code
from flask import Flask, render_template

# initializing
app = Flask(__name__)

# Home page, landing, index
@app.route('/')
def home():
    return render_template("home.html")

# Another one
@app.route('/another')
def another():
    return render_template("another.html")


# Run the app
if __name__ == '__main__':
    app.run(debug=True)