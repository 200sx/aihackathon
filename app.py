from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify, json
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/API')
def hello_world():
	api = "THIS API is HALO"
    return render_template("person.html", api=api )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

