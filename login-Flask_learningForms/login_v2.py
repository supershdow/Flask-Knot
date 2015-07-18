from flask import Flask, render_template, request
import Reader


login=Flask(__name__)


#username='supershdow'
#password='magic'
#Username and password constants used for verification later
#ARE VARIABLE
#credentials={}
#credentials['supershdow']='magic'


@login.route('/')
def root():
    return render_template('form.html')

@login.route('/login', methods=['POST','GET'])#Allows both Post (going through the form) and Get (going directly to the page)
def log_in():
    request_data=request.form#Takes the immutable dictionary of the user's inputs and saves it in a variable
    if request.method=="GET":
        return render_template('form.html', error='Please enter from the form on the main page')#Tells the user to go through the main page if they entered directly
    elif request.method=="POST":#Verifies the username and password against constants at the top
        credentials=Reader.getCsvDict('credentials.txt')
        if request_data['user'] in credentials and request_data['user']!='':
            if request_data['pswd']==credentials[request_data['user']][0]:
                return 'success'
            else:
                return render_template('form.html', error='Invalid username or password')
        else:
            return render_template('form.html', error='Invalid username or password')
    else:
        return 'yo'
@login.route('/signup', methods=['POST', 'GET'])
def signup():
    previousCredentials=Reader.read_file('credentials.txt')
    if request.method=="GET":
        return render_template('signup.html')
    elif request.method=="POST":
        new_user=request.form['nuser']
        new_pswd=request.form['npswd']
        new_credentials='%s,%s'%(new_user,new_pswd)
        if new_user=='' or new_pswd=='' or new_user in previousCredentials or new_user.find(',')!=-1 or new_pswd.find(',')!=-1:
            return render_template('form.html', error='Invalid signup credentials')
        else:
            Reader.write_file('credentials.txt',new_credentials,'a')
            return render_template('form.html', error='Successfully signed up')
    else:
        return 'yo'

if __name__=='__main__':
    login.debug=True
    login.run()
