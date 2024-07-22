from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase


Config = {
  "apiKey": "AIzaSyAEltzMtMRec4XoaGaPlb2tSo5cs-2izNc",
  "authDomain": "auth-lab-dfb29.firebaseapp.com",
  "projectId": "auth-lab-dfb29",
  "storageBucket": "auth-lab-dfb29.appspot.com",
  "messagingSenderId": "446682582871",
  "appId": "1:446682582871:web:3a7922d45379ebe74a7812",
  "databaseURL": ""
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

app = Flask(__name__, template_folder='Templates', static_folder='Static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signup():
  error=""
  if request.method == 'POST':
    email = request.form["email"]
    password = request.form["password"]
    try:
        session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('home'))
    except:
        error = "Authentication failed"
        print(error)
  return render_template("signup.html")



@app.route('/signin', methods=['GET', 'POST'])
def signin():
  error=""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('home'))
    except:
        error = "Authentication failed"
        print(error)
        return render_template("signin.html")
  return render_template("signin.html")


@app.route('/signout', methods=['GET', 'POST'])
def signout():
  session.pop('user', None)
  session.pop('quotes', None)
  session.modified = True 
  return redirect(url_for('signup'))
    

@app.route('/thanks')
def thanks():
  return render_template("thanks.html")


@app.route('/display')
def display():
  return render_template("display.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    quotes = request.form['quotes']
    session['quotes'].append(quotes)
    session.modified = True 
    return redirect(url_for('thanks'))
  return render_template("home.html")

    
if __name__ == '__main__':
  app.run(debug=True)