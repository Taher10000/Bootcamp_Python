from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)          
app.secret_key = 'wqwew'           
    



@app.route('/')                           
def index():
    if 'counter' in session:
        session['counter'] +=1
    else:
        session['counter'] = 0


    return render_template('index.html')  

@app.route('/counter', methods = ['POST'])
def counter():
    return redirect ('/')

@app.route('/twice', methods = ['POST'])
def twice():
    if 'counter' in session:
        session['counter'] +=1
    else:
        session['counter'] = 0
    return redirect ('/')

@app.route('/destroyer', methods = ['POST'])
def destroyer():
    session.clear()	
    session['counter'] = 0
    print(session['counter'])
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)                   

