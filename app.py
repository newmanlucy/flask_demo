from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_names = os.listdir('static')
    return render_template('images.html', image_names=image_names)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=81)
