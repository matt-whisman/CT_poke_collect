from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.blueprints.main.models import User


class RegistrationForm(FlaskForm):
    pass

    def validate_username(self, username):
        pass

    def validate_email(self, email):
        pass
