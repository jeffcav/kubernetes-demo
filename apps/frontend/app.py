import os
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
    time_server = os.environ.get('TIME_SERVER')
    
    current_time = requests.get("http://" + time_server).text

    html = "<html><body style=\"background-color:powderblue;\"><h1>Current time: {}</h1></body></html>\n".format(current_time)


    return html
