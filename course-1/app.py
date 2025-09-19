# Importing Flask
from flask import Flask, render_template

# Initialize the app
app = Flask(__name__)

# Making the Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Run the app in debug mode to see live updates/info in terminal
if __name__ == '__main__':
    app.run(debug=True)