from flask import Flask, render_template, request, redirect, url_for
import threading
import subprocess
import uuid



app = Flask(__name__)
backgroud_scripts = {}

def run_script(id):
	subpro

@app.route('/')
def main():
	return render_template('index.html')
@app.route('/choose/')
def choose():
	return render_template('choose.html')

	
@app.route('/choose/profession1/')
def profession1():
	return render_template('prof-Doctor-results.html')
@app.route('/choose/profession2/')
def profession2():
	return render_template('prof-Dentist-results.html')
@app.route('/choose/profession3')
def profession3():
	return render_template('prof-Lawyer-results.html')
@app.route('/choose/profession4/')
def profession4():
	return render_template('prof-Pharmacy-results.html')




if __name__ == '__main__':
	app.run()

