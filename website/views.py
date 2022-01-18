# ------------------------------------- #
# Store standard roots for the website: #
# Any page that isn't authentication    #
# related that users can navigate to.   #
# ------------------------------------- #
from flask import Blueprint
from flask import render_template

# define views file as blueprint (root)
views = Blueprint("views", __name__)


# create home page route (url)
@views.route("/")
def index():
    return render_template("public/index.html")


@views.route("/about")
def about():
    return"<h1 style='color:blue;'><strong>About Quicksave.io</strong></h1>"