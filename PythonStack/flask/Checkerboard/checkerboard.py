from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("board.html", width = 8, length = 8)

@app.route("/<int:num>")
def index1(num):
    times = int(num)
    return render_template("board.html", width = 8, length = times)

@app.route("/<int:width>/<int:hieght>")
def size(width, hieght):
    width = int(width)
    length = int(hieght)
    return render_template("board.html", width = width, length = length)

if __name__ == "__main__":
    app.run(debug=True)