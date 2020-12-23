import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://bsuwdgvzvurkpj:0383e6046646f9f6814adfe5da0deb777e24bc7fa41abd465a123d54850f73f6@ec2-18-211-171-122.compute-1.amazonaws.com:5432/dajp8dqbsg8d4s'
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
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes