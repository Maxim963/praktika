from flask import Flask, session

app = Flask(__name__)
app.secret_key = '999mmm666AAA333xxx'

@app.route('/setuser/<user>')
def setuser (user):
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser():
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    app.run(debug=True)