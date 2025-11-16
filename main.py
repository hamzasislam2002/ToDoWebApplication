from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def page():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def home():
    
    return render_template("login.html")

@app.route("/notesform")
def form():
    return render_template("notes_form.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/admin")
def admin():
    return redirect(url_for("page"))

@app.route("/<name>")
def fullname(name):
    return f"<h1>Hello</h1> {name}"

if __name__ == "__main__":
    app.run()