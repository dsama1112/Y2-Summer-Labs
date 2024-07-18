from flask import Flask, render_template, url_for, redirect, request
import random


app = Flask(__name__, template_folder = 'Templates', static_folder='Static')

@app.route('/home', methods= ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        birth=request.form['birth']
        return redirect(url_for("fortune", date=birth))



@app.route("/fortunetelling/<date>")
def fortune(date):

    fortunes10 = ["You're gonna slip off a banana and fall on your head..oops! ", 
    "You're gonna win the lottery tomorrow!! ", 
    "You're gonna find a bag full of gold coins soon.. ", 
    "You're gonna find your soulmate soon ", 
    "You're gonna fall in love soon.. ", 
    "Be careful of the close brunette in your life ", 
    "A blonde is gonna trick you ", 
    "The person you trust the most will betray you ", 
    "You're gonna get evicted soon ", 
    "Watch out for a red object that may change the course of your life "]

    fortunes11= "Watch out for the next blonde you become friends with.."

    # fortune_options = random.randint(0, len(date))
    dateoption = len(date)-1
    # dateoption = int(date)
    if dateoption < 10:
        datefinal= fortunes10[dateoption]
        return render_template("fortune.html", date_html=date, fortunetelling=datefinal)
    else:
        return fortunes11





if __name__ == '__main__':
     app.run(debug=True)