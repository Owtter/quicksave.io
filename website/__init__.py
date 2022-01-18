from flask import Flask


# create flask application and key
def create_app():
    app = Flask(__name__)
    # make mroe secret after testing
    app.config['SECRET_KEY'] = 'key'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app