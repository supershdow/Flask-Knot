from flask import Flask, render_template
from data import storygen_v4 as story

Proj1_v1=Flask(__name__)

@Proj1_v1.route('/')
def root():
    return render_template('main.html', title='Main Page')

@Proj1_v1.route('/rotn')
def rotn():
    return render_template('rotn.html', title='Caesar Cipher')

@Proj1_v1.route('/sengen')
def sengen():
    return render_template('sengen.html', title='Sentence Generator')

@Proj1_v1.route('/markov/')
@Proj1_v1.route('/markov/<text>')
def markov_result(text='all'):
    return render_template('markov.html', title='Markov Text Generator', book=text.capitalize())




if __name__=='__main__':
    Proj1_v1.debug=True
    Proj1_v1.run(host='0.0.0.0')
