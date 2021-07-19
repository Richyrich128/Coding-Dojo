from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
# no sescret key needed for this one
app.secret_key ="getit"
@app.route("/")
def add():
    if "number" not in session:
        session["number"] = 0
    
    session["number"] += 1
    return render_template("counter.html")

@app.route("/destroy_session")
def eliminate():
    session.pop("number")
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)    