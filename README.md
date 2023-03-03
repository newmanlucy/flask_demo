# flask_demo

## To run
Create a virtual environment with `python3 -m venv env` and activate it with `source env/bin/activate`. Install requirements with `pip instal -r requirements.text`.

Run the app with `python app.py` and view web page at localhost:81.

## Explanation
The main logic is in `app.py`. [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart) can [render templates](https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates) based on the Jinja templating language. It will look for templates in the `/templates` directory and image in the `/static` directory. The main function uses the `os` library to list files in the static directory and pass that list of file names into the template. The template then renders an `<img>` for each file name in the list. A file `flask_images_demo.html` will also be generated with the rendered html.
