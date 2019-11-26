from flask_avatars import Avatars
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
dropzone = Dropzone()
moment = Moment()
whooshee = Whooshee()
avatars = Avatars()
csrf = CSRFProtect()
migrate = Migrate()