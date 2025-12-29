from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWT
from flask_cors import CORS
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWT()





