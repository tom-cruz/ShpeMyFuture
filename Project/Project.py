from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')

def main():
	return render_template('index.html')
@app.route('/choose/')
def choose():
	return render_template('choose.html')
@app.route('/choose/profession1/')
def profession1():
	return render_template('profession1.html')
    
@app.route('/choose/profession2/')
def profession2():
	return render_template('profession2.html')
@app.route('/choose/profession3')
def profession3():
	return render_template('profession3.html')
@app.route('/choose/profession4/')
def profession4():
	return render_template('profession4.html')
if __name__ == '__main__':
	app.run()

