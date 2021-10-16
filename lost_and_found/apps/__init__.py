from  flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_wtf import CsrfProtect
from datetime import timedelta

from lost_and_found.apps.admin.view import bp_admin
from lost_and_found.apps.peizi import peize
from lost_and_found.apps.public.public import bp_bool
from lost_and_found.apps.user.blue_user import bp_user

def create_app():

    app=Flask(__name__,template_folder='../templates',static_folder='../static')
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_bool)
    app.register_blueprint(bp_admin)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/tree'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/tree'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_SECRET_KEY '] = 'sfgopd;asmfnpalafnsoufh;afsf'
    app.config['SECRET_KEY'] = 'oifjasf;lhfoamsfuheger'
    app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
    app.config['ALLOWED_EXTENSIONS']=set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    peize(app)

    return app