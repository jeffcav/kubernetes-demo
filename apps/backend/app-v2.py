from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
    now = datetime.now()
    
    # Changing the format of what is returned
    return now.strftime("%d/%m/%Y - %H:%M:%S")
