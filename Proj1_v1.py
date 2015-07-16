from flask import Flask, render_template

Proj1_v1=Flask(__name__)

@Proj1_v1.route('/')
def root():
    return "Hello Muhammad"






if __name__=='__main__':
    Proj1_v1.debug=True
    Proj1_v1.run(host='0.0.0.0')
