from flask import Flask, render_template, url_for, redirect, request
from flask import session as session
import pyrebase




Config = {
  "apiKey": "AIzaSyCz_lkkxNcF3Hfcuri5jx_m6AHnSQnHmQE",
  "authDomain": "y2-individual-summer-project.firebaseapp.com",
  "projectId": "y2-individual-summer-project",
  "storageBucket": "y2-individual-summer-project.appspot.com",
  "messagingSenderId": "397391175483",
  "appId": "1:397391175483:web:e6627ff2612088baee211e",
  "databaseURL": "https://y2-individual-summer-project-default-rtdb.europe-west1.firebasedatabase.app/"
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
  			user={"email": email, "password": password}
  			UID = session['user']['localId']
  			db.child("users").child(UID).set(user)
  			db.child("recipe").set({"Name": "Milkshake", 
  				"Ingredients": "1/4 cup milk, 3 tablespoons sugar, 2 cups halved fresh strawberries, 1-3/4 cups sliced peeled peaches (about 3 medium) or frozen unsweetened sliced peaches, thawed, 2 cups vanilla ice cream", 
  				"Instructions": "...."})
  			return redirect(url_for('category'))
  		except:
  			return "Authentication failed"
	return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error=""
	if request.method == 'POST':
		try:
			username = request.form['username']
			email = request.form['email']
			password = request.form['password']
			session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for("category"))
		except:
			return "Authentication failed"
	return render_template("signin.html")


@app.route('/category', methods=['GET', 'POST'])
def category():
	error=""
	if request.method == 'GET':
		return render_template("category.html")
	else:
		return render_template("category1.html")


@app.route('/category1', methods=['GET', 'POST'])
def category1():
	return render_template("category1.html")

    
if __name__ == '__main__':
	app.run(debug=True)