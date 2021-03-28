from flask import Flask,request,render_template,redirect,session

app=Flask(__name__)
app.secret_key="l;f2j;fs/.masdopff"

@app.route("/")
def home():
    if "status" in session:
         return redirect("http://127.0.0.1:3000/member")
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test":
        session["status"]=request.form["account"]
        return redirect("http://127.0.0.1:3000/member")
    else:
        return redirect("http://127.0.0.1:3000/error")

@app.route("/member")
def member():
    return render_template("right.html")

@app.route("/error")
def  error():
    return  render_template("wrong.html")

@app.route("/loggedout")
def loggedout():
    session.pop("status", None)
    return redirect("http://127.0.0.1:3000")


app.run(port=3000)

