import os
import imghdr
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


# create flask application and key
def create_app():
    app = Flask(__name__)
    # change to random b'' for productin
    app.config["SECRET_KEY"] = "key"
    app.config["UPLOAD_FOLDER"] = "uploaded-files"
    # TODO: adjust settings according to production environment
    # limit max upload size to 5mb
    app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 5
    # choose which file types can be uploaded
    app.config["UPLOAD_EXTENSIONS"] = [
        # image files
        ".jpg", ".png", ".gif", ".jpeg", ".psd",
        # text files
        ".doc", ".docx", ".odt", ".rtf", ".txt", ".pdf", ".xlsx", ".xls"
        # data files
                                                                  ".csv", ".pptx", ".xml",
        # audio files
        ".mp3", ".wav",
        # video files
        ".avi", ".flv", ".asf", ".mov", ".mp4", ".mpg", ".wmv",
        # 3D image files
        ".3dm", ".3ds", ".max", ".obj",
        # code files
        ".css", ".html", ".js", ".php", ".py", ".c", ".cpp", ".cs", ".java",
        ".lua",
        # other files
        ".zip", ".rar", ".zipx",
    ]

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


def save_file():
    form = UploadFileForm()
    app = create_app()

    if form.validate_on_submit():
        # fetch file
        file = form.file.data
        # save file
        for file in request.files.getlist("file"):
            file_name = secure_filename(file.filename)
            if file_name != "":
                file_ext = os.path.splitext(file_name)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"] or \
                    file_ext != validate_image(file.stream):
                    return "Invalid image", 400

                file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                       app.config["UPLOAD_FOLDER"],
                                       file_name))
    return '', 204
