from flask import render_template, request
from main import app

@app.route('/')
@app.route('/home/')
def home():
	return render_template('home.html')

@app.route('/resultado/',  methods=["GET", "POST"])
def resultado():
	if request.method == 'POST':
		formData = request.form
		json_result = dict(formData)
		print(json_result)
		return json_result

	