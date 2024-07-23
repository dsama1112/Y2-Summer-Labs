from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
import pyrebase




Config = {
  "apiKey": "AIzaSyAEltzMtMRec4XoaGaPlb2tSo5cs-2izNc",
  "authDomain": "auth-lab-dfb29.firebaseapp.com",
  "projectId": "auth-lab-dfb29",
  "storageBucket": "auth-lab-dfb29.appspot.com",
  "messagingSenderId": "446682582871",
  "appId": "1:446682582871:web:3a7922d45379ebe74a7812",
  "databaseURL": "https://database-lab-9f080-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='Templates', static_folder='Static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signup():
  error=""
  if request.method == 'POST':
    username = request.form['username']
    email = request.form["email"]
    password = request.form["password"]
    try:
        session['user'] = auth.create_user_with_email_and_password(email, password)
        user={"email": email,"password"}
        UID = login_session['user']['localId']
        db.child("users").child(UID).set(user)
        # return redirect(url_for('home'))

    except:
        error = "Authentication failed"
        print(error)

        if user in session:
        user_id = session['user']['localId']
        # user
  return render_template("signup.html")




    
if __name__ == '__main__':
  app.run(debug=True)