from flask import Flask, render_template

app = Flask(__name__)

console_data = {
    1: {'name': '패밀리컴퓨터', 'company': 'Nintendo', 'topTitle': {'드래곤퀘스트3': 1987, '파이널판타지3': 1990, '패미컴탐정클럽 Part2': 1989}},
    2: {'name': 'Play Station2', 'company': 'SONY', 'topTitle': {'바이오하자드4': 2006, '령 제로': 2001}}
}


@app.route('/')
def index():
    return render_template('index.html', consoles=console_data)


@app.route('/console/<int:id>')
def console(id):
    return render_template('console.html',
                           console_name=console_data[id]['name'],
                           console_title=console_data[id]['topTitle'])


if __name__ == '__main__':
    app.run(debug=True)
