from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

accounts = sqlite3.connect("accounts.db")
videos = sqlite3.connect("videos.db")
accountsCur =accounts.cursor()
videosCur = videos.cursor()



@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

