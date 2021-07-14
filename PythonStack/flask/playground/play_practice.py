from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play1():
    return render_template("play.html",num=3,color="blue")

@app.route("/play/<int:num>")
def play2(num):
    times = int(num)
    return render_template("play.html",num=times,color="blue")

@app.route("/play/<int:num>/<color>")
def play3(num, color):
    times = int(num)
    c = color
    return render_template("play.html",num=times,color=c)

if __name__ == "__main__":
    app.run(debug=True)