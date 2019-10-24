from flask import Flask, render_template, request, escape
from vsearch import letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as logs:
        print(req.form, req.remote_addr, req.user_agent, res, file=logs, sep='|')

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
    return render_template('entry.html', the_title='Привет Анзор! Найди общие буквы или цифры:')

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
                           the_title='Логи',
                           the_row_titles=titles,
                           the_data=contents, )

if __name__ == '__main__':
    app.run(debug=True)