from flask import Flask, request,session 
from flask import render_template

app = Flask(__name__)
app.secret_key="coolkid"

@app.route("/")
def index():
  return render_template("home.html")

@app.route("/form.html",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "12345":
      error = name+", dude, try again(hint, it's 12345)"
      name=""
    else: 
      error = "Cool! I haven't figured this out yet so just erase form.html up top and add session.html instead. Enjoy!"
      
    return render_template("form.html",error=error, name=name)

@app.route("/session.html")
def session_demo():

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session.html',count = session['count'])
 


app.run(host="0.0.0.0",port=5000,debug=True)