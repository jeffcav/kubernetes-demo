from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
    now = datetime.now()
    return now.strftime("%d/%m/%Y - %H:%M:%S")
