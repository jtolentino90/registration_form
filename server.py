from flask import Flask, render_template, session, redirect, request, flash
import re
app = Flask(__name__)
app.secret_key = "ThisSecretKey"

#list of regex operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	print request.form
	error = 0;

	#first name
	if len(request.form['first']) < 1:
		flash("Please enter a first name!")
		error += 1
	elif not NAME_REGEX.match(request.form['first']):
		flash("Name cannot contain numbers!")
		error += 1

	#last name
	if len(request.form['last']) < 1:
		flash("Please enter a last name!")
		error += 1
	elif not NAME_REGEX.match(request.form['last']):
		flash("Name cannot contain numbers!")
		error += 1

	#email
	if len(request.form['email']) < 1:
		flash("Email cannot be empty.")
		error += 1
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		error += 1

	#password
	if len(request.form['password']) < 8:
		flash("Password must be at least 8 characters!")
		error += 1
	if request.form['password'] != request.form['password2']:
		flash("Please re-enter password.")
		error += 1

	#redirect if there are no errors
	if error == 0:
		return redirect('/finished')

	return redirect('/')

@app.route('/finished')
def finished():
	return render_template('finished.html')

app.run(debug=True)
