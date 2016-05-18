from flask import Flask, render_template, redirect,url_for,request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "never guess "

#login required decorator
def  login_required(f):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        flash('you need to login first.')
        return redirect(url_for('login'))
return wrap

@app.route('/')
def home():
   #return "Hello, world!"
   return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	session['logged_in']= True
        flash('You have logged in ')
        return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)

        flash('You have logged out')
	return redirect(url_for('welcome'))



if __name__ == '__main__':
    app.run(debug = True) 