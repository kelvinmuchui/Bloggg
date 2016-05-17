from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	return render_template('login.html')
if __name__ == '__main__':
    app.run(debug = True) 