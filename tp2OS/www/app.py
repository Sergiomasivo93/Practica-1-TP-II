from aux_pro import Process
from flask import Flask
from flask import render_template
from database import Database
from models import Samples

app = Flask(__name__)
db  = Database()
pro = Process()
 
 
@app.route('/')
def index():
	idd=0
	last=0
	last_ten=0

	if not pro.is_running():
		idd=pro.start_process() #arrancar el process.py por primera y unica vez
	else:
		last = db.get_last()
		last_ten = db.get_last_ten()
	return render_template('index.html',l=last,t=last_ten)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8888)
