import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://dfmpwulvaqkfii:f0890fee881e6ee3bebb46616f53e154f666313d796fdc131bab9bd484b4ce66@ec2-52-44-235-121.compute-1.amazonaws.com:5432/d6skm3id6meq23'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# heroku = Heroku(app)
# db = SQLAlchemy(app)
# db.init_app(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.zoho.in'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('BLOGIFI_MAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('BLOGIFI_PASS')
mail = Mail(app)


from flaskblog import routes