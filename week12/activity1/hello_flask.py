from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return render_template("index.html")

@app.route("/bye")
def goodbye_flask():
    return "<p>Goodbye, flask!</p>"


@app.route("/username/<name>/<int:number>")
def Learn(name, number):
    return f"{name} is learning flask, he wakes up early in the morning and goes to bed late at night. He practices for {number} hours every day."

@app.route("/learnmore")
def learnmore():
    return "<title>Learn More</title> <p> if you want to learn more, click on the link below</p> <a href='https://flask.palletsprojects.com/en/stable/quickstart/#'>https://flask.palletsprojects.com/en/stable/quickstart/#</a>"

if __name__ == "__main__":
    app.run(debug=True)