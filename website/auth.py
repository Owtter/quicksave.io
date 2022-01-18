from flask import Blueprint

# define auth file as blueprint (root) for authentication pages
auth = Blueprint("auth", __name__)


# page to sync devices and enable server access
@auth.route("/sync")
def sync():
    return"<h1>Sync</h1>"


# page to see synced devices, etc.
@auth.route("/profile")
def profile():
    return"<h1>This page will allow you to see all of your synced devices!</h1>"



