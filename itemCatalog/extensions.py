from flask_login.login_manager import LoginManager

from itemCatalog.models import User



login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(userId):
    return User.query.get(userId) 
