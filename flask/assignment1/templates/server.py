import re
from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 

   # Create a new instance of the Flask class called "app"





@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/taher')
def taher():
    return 'Hello taher!'

@app.route('/name/<name>/<age>')
def name_age(name,age):
    print(name)
    print(age)
    return f"Hello I am {name} and I am {age} old!"

@app.route('/name/<name>/<int:age>')
def name_age2(name,age):

    #rendering template page and passing some arguments
    return render_template('people.html',name = name, age = age)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



