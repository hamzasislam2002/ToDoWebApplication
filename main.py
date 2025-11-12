from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/notesform")
def formnotes():
    return render_template("notes_form.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/notes")
def note():
    return render_template("notes.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()