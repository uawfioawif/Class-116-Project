# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Joe" # write your name
    age = "5" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def fatherFlask() :
    name = "Joe" # write your name
    age = "53" # write your age
    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def motherFlask() :
    name = "Pam" # write your name
    age = "55" # write your age
    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friendsFlask() :
    name = "Jeff" # write your name
    age = "6" # write your age
    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
