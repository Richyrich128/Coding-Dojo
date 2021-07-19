from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    apple = request.form["apple"]
    num = int(strawberry) + int(raspberry) + int(apple)
    
    first = request.form["first_name"]
    last = request.form["last_name"]
    idd = request.form["student_id"]
    
    return render_template("checkout.html", strawberry = strawberry, raspberry = raspberry, apple = apple, first = first, last = last, idd = idd, num = num)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    