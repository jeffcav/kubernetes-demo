import os
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
    time_server = os.environ.get('TIME_SERVER')
    
    current_time = requests.get("http://" + time_server).text

    return "CURRENT TIME: " + current_time
