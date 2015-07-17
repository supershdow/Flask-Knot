from flask import Flask, render_template, request
import Reader


login=Flask(__name__)


username='supershdow'
password='magic'
#Username and password constants used for verification later
#ARE VARIABLE
credentials={}



@login.route('/')
def root():
    return render_template('form.html')

@login.route('/login', methods=['POST','GET'])#Allows both Post (going through the form) and Get (going directly to the page)
def log_in():
    request_data=request.form#Takes the immutable dictionary of the user's inputs and saves it in a variable
    if request.method=="GET":
        return render_template('form.html', error='Please enter from the form on the main page')#Tells the user to go through the main page if they entered directly
    elif request.method=="POST":#Verifies the username and password against constants at the top
        if request_data['user']==username and request_data['pswd']==password:
            return 'success'
        else:
            return render_template('form.html', error='Invalid username or password')
    else:
        return 'yo'
@login.route('/signup')
def signup():
    return 'yo'


if __name__=='__main__':
    login.debug=True
    login.run()
