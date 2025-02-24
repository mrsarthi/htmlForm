from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    name = email = message = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
    return render_template("form.html", name=name, email=email, message=message)


if __name__ == "__main__":
    app.run(debug=True)
