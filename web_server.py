from flask import Flask, render_template, request, redirect
from csv import writer

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
	return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_file(data)
    	return redirect('thankyou.html')
    else:
    	return "Something went wrong..."

def write_to_file(data):
	with open('database.csv', "a") as database:
		csv_writer = writer(database)
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer.writerow([email, subject, message])
	