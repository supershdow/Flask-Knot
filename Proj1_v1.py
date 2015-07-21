from flask import Flask, render_template, request
from data import sentencegenerator as story
from data import Reader,cipher,markov_v3 as chain


Proj1_v1=Flask(__name__)

@Proj1_v1.route('/')
def root():
    return render_template('main.html', title='Main Page')

def numCheck(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


@Proj1_v1.route('/rotn', methods=["POST","GET"])
def rotn():
    if request.method=="GET":
        return render_template('rotn.html', title='Caesar Cipher')
    elif request.method=="POST":
        request_data=request.form
        if numCheck(request_data['key']):
            if abs(int(float(request_data['key'])))<100:
                   cypher=cipher.rotn(request_data['word'],int(float(request_data['key'])))
                   return render_template('rotn.html', title='Caesar Cipher', error=cypher)
            else:
                return render_template('rotn.html', title='Caesar Cipher', error='Key too large or too small')
        else:
            return render_template('rotn.html', title='Caesar Cipher', error='Not a valid key')
    else:
        return 'yo'


@Proj1_v1.route('/sengen', methods=['POST','GET'])
def sengen():
    if request.method=="GET":
        return render_template('sengen.html', title='Sentence Generator', Sentences='')
    elif request.method=="POST":
        sentences=request.form
        if numCheck(sentences['numsen']):
            if int(float(sentences['numsen']))>50:
                return render_template('sengen.html', title='Sentence Generator', Sentences=story.senGen(50), error="Input too high. Generating 50 sentences")
            elif int(float(sentences['numsen']))<0:
                return render_template('sengen.html', title='Sentence Generator', error='Invalid number of sentences')
            else:
                return render_template('sengen.html', title='Sentence Generator', Sentences=story.senGen(int(float(sentences['numsen']))))
        else:
            return render_template('sengen.html', title='Sentence Generator', error='Invalid number of sentences')
        
    else:
        return 'yo'


@Proj1_v1.route('/markov/', methods=['POST',"GET"])
def markov():
    if request.method=='GET':
        return render_template('markov.html', title='Markov Text Generator', book='', text='', image='Josh')
    elif request.method=='POST':
        book=request.form['booklist']
        if book!='Select':
            return render_template('markov.html', title='Markov Text Generator', book=book, text=chain.markov_generator(book), image=book)
        else:
            return render_template('markov.html', title='Markov Text Generator', text='Not a valid input', image='Josh')
    else:
        return 'yo'


def validate(u,p):
    request_data=request.form
    credentials=Reader.getCsvDict('./data/credentials.txt')
    if request_data['user'] in credentials and request_data['user']!='':
        if request_data['pswd']==credentials[request_data['user']][0]:
            return True
        else:
            return False
    else:
        return False

@Proj1_v1.route('/login', methods=['POST','GET'])#Allows both Post (going through the form) and Get (going directly to the page)                                                           
def log_in():
    if request.method=="GET":
        return render_template('form.html', title='login')                        
    elif request.method=="POST":#Verifies the username and password against constants at the top
        request_data=request.form#Takes the immutable dictionary of the user's inputs and saves it in a variable
        credentials=Reader.getCsvDict('./data/credentials.txt')
        if validate(request_data['user'],request_data['pswd']):
            return render_template('form.html', title='login', error='Successful login')
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
            Reader.write_file('./data/credentials.txt',new_credentials+'\n','a')
            return render_template('form.html', error='Successfully signed up!', title='Login')
    else:
        return 'yo'


if __name__=='__main__':
    Proj1_v1.debug=True
    Proj1_v1.run(host='0.0.0.0')
