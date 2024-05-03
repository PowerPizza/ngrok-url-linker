from flask import Flask, render_template, request
import json

app = Flask(__name__)

current_url = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_url", methods=["POST"])
def get_url():
    return current_url

@app.route("/set_url", methods=["POST"])
def set_url():
    global current_url
    current_url = json.loads(request.data.decode())["url"]
    return "200"

app.run(debug=True)