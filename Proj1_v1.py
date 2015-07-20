from flask import Flask, render_template, request
from data import sentencegenerator as story
from data import Reader
from data import cipher


Proj1_v1=Flask(__name__)

@Proj1_v1.route('/')
def root():
    return render_template('main.html', title='Main Page')

@Proj1_v1.route('/rotn', methods=["POST","GET"])
def rotn():
    if request.method=="GET":
        return render_template('rotn.html', title='Caesar Cipher')
    elif request.method=="POST":
        request_data=request.form
        if request_data['key'].isdigit()==True:
            cypher=cipher.rotn(request_data['word'],int(request_data['key']))
            return cypher
        else:
            return render_template('rotn.html', title='Caesar Cipher', error="Not a valid key")
    else:
        return 'yo'


@Proj1_v1.route('/sengen')
def sengen():
    return render_template('sengen.html', title='Sentence Generator', Sentences=story.senGen(5))


@Proj1_v1.route('/markov/')
@Proj1_v1.route('/markov/<text>')
def markov_result(text='all'):
    return render_template('markov.html', title='Markov Text Generator', book=text.capitalize())

@Proj1_v1.route('/login', methods=['POST','GET'])#Allows both Post (going through the form) and Get (going directly to the page)                                                           
def log_in():
    if request.method=="GET":
        return render_template('form.html', title='login')                        
    elif request.method=="POST":#Verifies the username and password against constants at the top
        request_data=request.form#Takes the immutable dictionary of the user's inputs and saves it in a variable
        credentials=Reader.getCsvDict('./data/credentials.txt')
        if request_data['user'] in credentials and request_data['user']!='':
            if request_data['pswd']==credentials[request_data['user']][0]:
                return 'success'
            else:
                return render_template('form.html', error='Invalid username or password', title='Login')
        else:
            return render_template('form.html', error='Invalid username or password', title='Login')
    else:
        return 'yo'

@Proj1_v1.route('/signup', methods=['POST', 'GET'])
def signup():
    previousCredentials=Reader.read_file('./data/credentials.txt')
    if request.method=="GET":
        return render_template('signup.html', title='Sign up')
    elif request.method=="POST":
        new_user=request.form['nuser']
        new_pswd=request.form['npswd']
        new_credentials='%s,%s'%(new_user,new_pswd)
        if new_user=='' or new_pswd=='' or new_user in previousCredentials or new_user.find(',')!=-1 or new_pswd.find(',')!=-1:
            return render_template('form.html', error='Invalid signup credentials', title='Login')
        else:
            Reader.write_file('./data/credentials.txt',new_credentials,'a')
            return render_template('form.html', error='Successfully signed up!', title='Login')
    else:
        return 'yo'


if __name__=='__main__':
    Proj1_v1.debug=True
    Proj1_v1.run(host='0.0.0.0')
