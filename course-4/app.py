# Import/Init
from flask import Flask, render_template, request
app = Flask(__name__)


# Get user data, notice the use of .get() and .post()
@app.get('/')
def getData():
    return render_template("getData.html")


# We'll explain error and data handling in the login video
@app.post('/')
def another():
    # Grabs the user data from the HTML form, stores it here, then we push it out
    name = request.form.get('name', 'Did Not Submit')
    age = request.form.get('age', 'Did Not Submit')
    favTeam = request.form.get('favTeam', 'Did Not Submit')

    return render_template("showData.html", name=name, age=age, favTeam=favTeam)


'''Another way:
@app.get('/', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        return render_template("getData.html")

    else:
        name = request.form.get('name', 'Did Not Submit')
        age = request.form.get('age', 'Did Not Submit')
        favTeam = request.form.get('favTeam', 'Did Not Submit')

        return render_template("showData.html", name=name, age=age, favTeam=favTeam)
'''


# Run app
if __name__ == '__main__':
    app.run(debug=True)