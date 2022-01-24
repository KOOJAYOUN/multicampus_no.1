from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route("/")
def FlaskLab():
    return "Flask 데이터 응답"

@app.route("/data1")
def FlaskData():
    keyValue = r"4jUGcCMfJnRYQr%2B6BjblUqAXZjXvoUkxOxplWYSCyE960crnJdxex2zQtXdBj68ZICDTuUwLqRo6mGiqdDy1HQ%3D%3D"

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond=" + "강남구"
    dataURL += "&serviceKey=" + keyValue
    
    dataResult = requests.get(dataURL)

    return json.loads(dataResult)
