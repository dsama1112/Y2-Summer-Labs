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
  			# db.child("users").child(UID).set(user)
  			# db.child("recipe").set({"Name": "Milkshake", 
  			# 	"Ingredients": "1/4 cup milk, 3 tablespoons sugar, 2 cups halved fresh strawberries, 1-3/4 cups sliced peeled peaches (about 3 medium) or frozen unsweetened sliced peaches, thawed, 2 cups vanilla ice cream", 
  			# 	"Instructions": "...."})
  			return redirect(url_for('category'))
  		except:
  			return "Authentication failed"
	return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error=""
	if request.method == 'POST':
		try:
			email = request.form['email']
			password = request.form['password']
			session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for("category"))
		except:
			return "Authentication failed"
	return render_template("signin.html")


@app.route('/category', methods=['GET', 'POST'])
def category():
	return render_template("category.html")


@app.route('/category1', methods=['GET', 'POST'])
def category1():
	error=""
	# show_rec= db.child("recipe").get().val()
	if request.method == 'POST':
		return render_template("category1.html")
	return render_template("category1.html")


@app.route('/category2', methods=['GET', 'POST'])
def category2():
	error=""
	show_rec= db.child("recipe").get().val()
	if request.method == 'POST':
		print(show_rec)
		return render_template("category2.html", show_rec=show_rec)
	return render_template("category2.html", show_rec=show_rec)


@app.route('/category3', methods=['GET', 'POST'])
def category3():
	error=""
	show_rec= db.child("recipe").get().val()
	if request.method == 'POST':
		print(show_rec)
		return render_template("category3.html", show_rec=show_rec)
	return render_template("category3.html", show_rec=show_rec)


@app.route('/review', methods=['GET', 'POST'])
def review():
	error=""
	if request.method == 'POST':
		comment = request.form['comment']
		comment_from = request.form['comment_from']
		UID = session['user']['localId']
		comments = {"Name:": comment_from, "Comment:": comment}
		db.child("comments").push(comments)
		return redirect(url_for('review'))
	return render_template("review.html")


@app.route('/view', methods=['GET', 'POST'])
def view():
	error=""
	show_comments= db.child("comments").get().val()
	print(show_comments)
	return render_template("view.html", show_comments=show_comments)
	if request.method=='POST':
		try:
			comment2 = request.form['comment']
			comment_from2 = request.form['comment_from']
			UID = session['user']['localId']
			comments2 = {"Name:": comment_from, "Comment:": comment}
			db.child("comments2").child(UID).remove()
			return render_template("view.html", comments2=comments2)
			print(comments2)
		except:
			error = "Couldn’t remove object"
		return "Authentication Failed"

# try:
# 	UID = login_session['user']['localId']
# db.child("Users").child(UID).remove()
# return redirect(url_for('signin'))
# except:
# error = "Couldn’t remove object"

if __name__ == '__main__':
	app.run(debug=True)