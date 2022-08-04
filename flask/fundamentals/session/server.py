from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'qwerty111'

@app.route('/')
def index():
    name = 'taher'
    return render_template("index.html", name=name)	

@app.route('/process_info', methods = ['POST'])
def process_info():
    print(request.form['credit_card_num'])
    session['ccn'] = request.form['credit_card_num'][-4:]
    print("got post info ",request.form)
    return redirect("/tracking") 

@app.route('/tracking') 
def tracking():
    print("your card num is: ",  session['ccn'])
    if 'ccn' not in session:
        return redirect('/')
    return render_template('tracking.html')
if __name__=="__main__":
    app.run(debug=True)