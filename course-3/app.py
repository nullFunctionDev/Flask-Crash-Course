from flask import Flask, render_template
app = Flask(__name__)


# Pages
name = "nullFunctionDev()"
@app.route('/')
def home():
    return render_template("home.html", person=name)


@app.route('/another')
def another():
    return render_template("another.html")


if __name__ == '__main__':
    app.run(debug=True)