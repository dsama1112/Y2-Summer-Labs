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
    full_name = request.form['full_name']
    email = request.form["email"]
    password = request.form["password"]
    try:
        session['user'] = auth.create_user_with_email_and_password(email, password)
        user={"email": email,"password": password}
        UID = session['user']['localId']
        db.child("users").child(UID).set(user)
        return redirect(url_for('home'))

    except:
        error = "Authentication failed"
        print(error)

        # if user in session:
        # user_id = session['user']['localId']
        # user
  return render_template("signup.html")


# @app.route('/')
# def index():
#     if 'user' in login_session:
#         print(login_session['user'])
#         user_id = login_session['user']['localId']
#         user_data = db.child("users").child(user_id).get().val()
#         all_users = db.child("users").get().val()
#         return render_template('profile.html', user=user_data, all_users=all_users)
#     return render_template('index.html')



# Right after you get the email and password from the form, create a dictionary called user that contains the keys full_name, email, and username as keys and the corresponding user inputs as values.
# Add the user dictionary you made to the database through the child Users and using the uid from session['user'] as the ID.


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
    quote = request.form['quotes']
    # session['quotes'].append(quotes)
    quote_from = request.form['quote_from']
    UID = session['user']['localId']
    quotes = {"text": quote, "said_by": quote_from, "uid": UID}
    db.child("quotes").push(quotes)    

    # for i in range(num_entries):
    # key = input("Enter key: ")
    # value = input("Enter value: ")
    # user_dict[key] = value
 
    #session.modified = True 
    return redirect(url_for('thanks'))
  return render_template("home.html")


#   In the /home route of app.py:

# Delete the code where you stored the quote in the session.
# Create a dictionary called quote that contains the keys 'text' and 'said_by' with values coming from the user inputs.
# Add a key uid to the dictionary quote whose value is the uid of the current user from the session
# Add the quote to the database using the child Quotes with a random key.

    
if __name__ == '__main__':
  app.run(debug=True)