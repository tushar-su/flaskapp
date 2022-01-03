from flask import Flask,  render_template

import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=c9Sy21jBq1Vumznzj8hk1mZvIyGilCK15uGrhrE0')
    response = r.json()
    copyright= response.get ("copyright")
    description= response.get ("explanation")
    title= response.get ("title")
    media= response["media_type"]
    url= response ["hdurl"]
  
    return render_template("home.html" ,
        copyright= copyright,        
        description= description,
        title= title,
        media= media,
        url= url)

