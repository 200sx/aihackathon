from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify, json
)
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("home.html")


@app.route('/API')
def apifunc():
	api = "THIS API is HALO"
	url = "https://el0yb5zcg9.execute-api.ap-southeast-2.amazonaws.com/default"
	payload={"data": "137,10232,55,1,2,1,0,1,44,0,5000,3,1,250,40,9.3333333,0.8"}

	r = requests.post(url, data=json.dumps(payload))
	result = r.json()
	result = result["predictions"][0]["score"]

	return render_template("person.html", api=result )

@app.route('/search', methods=('GET', 'POST') )
def searchfun():
	if request.method == 'POST':
		name = request.form[ 'user_id' ]
		return render_template("person.html", api=name )

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

