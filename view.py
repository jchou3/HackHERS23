from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home(): 
   # return "<center><h1>Welcome to HackHers23 unnamed<h1></center>"
    return render_template("view.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
