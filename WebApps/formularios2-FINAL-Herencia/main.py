from flask import Flask, render_template,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = "Supercalifragilisticoespialidoso"

@app.route("/")
def home():
    return render_template('index.html')
    

@app.route("/login",methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("acierto.html")
        else:
            return render_template("denegado.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

