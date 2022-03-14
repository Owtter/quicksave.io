# ------------------------------------- #
# Store standard roots for the website: #
# Any page that isn't authentication    #
# related that users can navigate to.   #
# ------------------------------------- #
import os
from flask import Blueprint, render_template
from website import save_file, UploadFileForm

# define views file as blueprint (root)
views = Blueprint("views", __name__)


# create home page route (url)
@views.route("/", methods=["GET", "POST"])
def index():
    save_file()

    return render_template("public/index.html", form=UploadFileForm())


@views.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@views.route("/about")
def about():
    return"<h1 style='color:blue;'><strong>About Quicksave.io</strong></h1>"

