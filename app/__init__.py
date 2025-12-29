from flask import flask, Blueprint 

bp  = Blueprint('blueprint', __name__ )


#flask app factory 
def create_app(config):
    app = Flask(__name__)
    
    app.register_blueprint(blueprint.auth)
