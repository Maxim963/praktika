from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = '999mmm666AAA333xxx'

@app.route('/')
def hello():
    return 'Hello Max, I know you!'

@app.route('/page1')
@check_logged_in
def page1():
    return 'This is - Page1'

@app.route('/page2')
@check_logged_in
def page2():
    return 'This is - page2'

@app.route('/page3')
@check_logged_in
def page3():
    return 'This is - page3'

@app.route('/page4')
def page4():
    return 'This is - page4'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'

# @app.route('/status')
# def do_status():
#     if 'logged_in' in session:
#         return 'Vot vam!'
#     return 'Hren Vam!!!'

if __name__ == '__main__':
    app.run(debug=True)