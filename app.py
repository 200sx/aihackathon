from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify, json
)
import requests
import json

app = Flask(__name__)

ID = {
    "10124": "77,10124,72,1,2,0,0,0,45,0,40000,1,1,6,21,9.333333333,0",
    "19148": "137,19148,72,1,2,1,0,1,31,0,20000,4,1,250,21,10,0.6,1",
    "19864": "87,19864,4,4,1,0,0,0,31,0,0,4,1,250,6,4.666666667,0"

}

Personal = {
    "10124": {
        "firstname": "Gamora",
        "lastname": "Mohegan",
        "email": "GaryJMohegan@gmail.com",
        "age": 49,
        "race": "Native American",
        "gender": "female",
        "income": "$100 000+",
        "education": "Bachelors Degree",
        "city": "St Louis",
        "postcode": "63108"
    },
    "19148": {
        "firstname": "Caroline",
        "lastname": "Ardist",
        "email": "CarolineJArdist@dayrep.com",
        "age": 31,
        "race": "Caucasian or White",
        "gender": "male",
        "income": "$20 000- $30 000",
        "education": "Associate Degree",
        "city": "North Kansa City",
        "postcode": 64116
    },
    "19864": {
        "firstname": "Augustina",
        "lastname": "Boles",
        "email": "AugustinaMBoles@einrot.com",
        "age": 31,
        "race": "Latino or Hispanic",
        "gender": "male",
        "income": "Unspecified",
        "education": "Associates Degree",
        "city": "St. Petersburg",
        "postcode": 33716
    }
}


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

		url = "https://el0yb5zcg9.execute-api.ap-southeast-2.amazonaws.com/default"

		payload={"data": ID[name]}

		r = requests.post(url, data=json.dumps(payload))
		result = r.json()
		result = result["predictions"][0]["score"]



		return render_template("person.html", api=result, details=Personal[name] )




if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

