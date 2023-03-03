from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_names = os.listdir('static')
    image_urls = ['static/' + name for name in image_names]
    rendered_template = render_template('images.html', image_urls=image_urls)
    with open('flask_images_demo.html', 'w') as f:
        f.write(rendered_template)
    return rendered_template

if __name__=='__main__':
    app.run(host='0.0.0.0', port=81)
    print("hi")
