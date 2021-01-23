from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

# bare extension instances
fbcrypt = Bcrypt()
ma = Marshmallow()
db = SQLAlchemy()
