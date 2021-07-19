from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = "secret_key"

@app.route("/")
def form():
    return render_template("index.html")

# this is for a post which should redirect to result
@app.route("/process", methods = ["POST"])
def process():
    session["users_name"] = request.form["users_name"]
    session["locations"] = request.form["locations"]
    session["languages"] = request.form["languages"]
    session["comments"] = request.form["comments"]
    
    return redirect("/result")

# using sesssion to get /process post info to display
@app.route("/result")
def result():
    return render_template("display_result.html")

if __name__=="__main__":
    app.run(debug=True) 