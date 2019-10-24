from flask import Flask, render_template, request, escape
from vsearch import letters
import mysql.connector
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1', 'user': 'adminmax', 'password': 'maxadmin999', 'database': 'logidb'}

def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': '127.0.0.1',
                'user': 'adminmax',
                'password': 'maxadmin999',
                'database': 'logidb', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letter'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()
    cursor.close()
    conn.close()

    # with UseDatabase(app.config['dbconfig']) as cursor:
    #     #     _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
    #     #     cursor.execute(_SQL, (req.form['phrase'], req.form['letter'],
    #     #                           req.remote_addr, req.user_agent.browser, res,))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letter = request.form['letter']
    title = 'Вот Ваш результат:'
    result = str(sorted(letters(phrase, letter)))
    log_request(request, result)
    return render_template('results.html', the_letters = letter, the_results = result,
                           the_title = title, the_phrase = phrase)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Привет Анзор! Найди общее во фразах с твоим именем или любым другим словом:')

@app.route('/logi')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('logi.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )

    # with UseDatabase(app.config['dbconfig']) as cursor:
    #     _SQL = """select phrase, letters, ip, browser_string, results from log"""
    #     cursor.execute(_SQL)
    #     contents = cursor.fetchall()
    # titles = ('Phrase', 'Letter', 'Remote_addr', 'User_agent', 'Results')
    # return render_template('logi.html',
    #                        the_title='Логи',
    #                        the_row_titles=titles,
    #                        the_data=contents)
if __name__ == '__main__':
    app.run(debug=True)