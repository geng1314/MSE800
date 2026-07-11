from flask import Flask, render_template
from flask import request

app = Flask(__name__)


def calculate_bmi(weight, height):
    """Calculate BMI and return category"""
    bmi = weight / (height**2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            if weight <= 0 or height <= 0:
                error = "Please enter positive values for weight and height."
                return render_template("index.html", error=error)
            bmi, category = calculate_bmi(weight, height)
            return render_template("result.html", bmi=bmi, category=category)
        except ValueError:
            error = "Please enter valid numbers for weight and height."
            return render_template("index.html", error=error)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
