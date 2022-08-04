from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)          
app.secret_key = 'wqwew12345'           
    



@app.route('/')                           
def index():

    return render_template('index.html')  

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect ('/result')
    
@app.route('/result')
def result():
    print("Name: ", session['name'])
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)                   

