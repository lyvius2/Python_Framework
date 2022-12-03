from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return '''
    <h1>제목</h1>
    <p>본문</p>
    '''


@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'


if __name__ == '__main__':
    app.run(debug=True)
