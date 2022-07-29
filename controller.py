from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('mainpage.html', **locals())

@app.route('/hackathons')
def hackathons():
	return render_template('hackathons.html', **locals())

@app.route('/meetings')
def meetings():
	return render_template('meetings.html', **locals())

if __name__ == "__main__":
	app.secret_key = 'byubyu9jujujhjuh'
	app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)