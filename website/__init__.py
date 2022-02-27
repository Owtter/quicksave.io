import os
from flask import Flask
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


# create flask application and key
def create_app():
    app = Flask(__name__)
    # change to random b'' for productin
    app.config['SECRET_KEY'] = 'key'
    app.config["UPLOAD_FOLDER"] = "static/uploaded-files"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


def save_file():
    form = UploadFileForm()
    app = create_app()

    if form.validate_on_submit():
        # fetch the file
        file = form.file.data
        # save the file

        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               app.config["UPLOAD_FOLDER"],
                               secure_filename(file.filename)))
