from flask import Flask, redirect, url_for, render_template, request, session, make_response
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Hello_Ashish_thisismysecretkey"
app.permanent_session_lifetime = timedelta(minutes=5)  # set lifetime of session



@app.route('/')
def home():
    # check if session available or not
    if "username" in session:
        return redirect(url_for('user'))
    else:
        return render_template('index.html')

# user login and create session
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True  # setting session True which is valid for certain time
        username = request.form['username']
        password = request.form['password']
        if username == "ashish" and password == "ashish@1":  # validate username and password
            session['username'] = username  # create session and store username
            return redirect(url_for('user'))  # redirect to the user page
        else:
            return 'username or password not matched!'
        
    else:
        if "username" in session:  # check if session data present or not
            return redirect(url_for('user'))  # redirect to the user page
        return render_template('index.html')

# if session is available then no need to login
@app.route('/user')
def user():
    if "username" in session:
        usr = session['username']
        return f"<h1> welcome {usr}</h1>"
    else:
        return redirect(url_for('login'))

# destoy session
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
