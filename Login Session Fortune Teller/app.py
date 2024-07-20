from flask import Flask, url_for, redirect, request
from flask import session as login_session

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        birthmonth = request.form['birthmonth']
        return render_template('home2.html')


 @app.route('/home')
def home():
   if 'name' in login_session:
       if login_session['admin'] == True:
           return render_template("adminPage.html")
   return render_template("userPage.html")

       
#         return redirect(url_for('response',
#             n = name,
#             s = animal))

# 3. Add the main route ‘/’ to app.py that renders a page login.html when a GET request comes in. When a 
# POST request comes in, it should store the name and month in the session and send the user to the /home route

# 4. Edit the home.html page to remove the form. Instead, display the text “Hello ____” where the ____ is the name the user submitted,
#  and a link (using the <a> tag) leading them to the /fortune route

# 5. Edit the /fortune route so that it no longer gets the birth month from the previous form, instead it should get the birth month 
# from the session (tha was entered in the login page). It should still use the length of the month to choose the fortune and 
# display it in fortune.html




