from flask import Flask,session
import os

app = Flask(__name__)

@app.route('/')

def func():
    app.secret_key = os.urandom(32)
    session['coke'] = 'pepsi'
    print(session['coke'])

if __name__ == "__main__":
    app.debug=True
    app.run()


