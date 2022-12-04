from flask import Flask, render_template
import requests

app = Flask(__name__)

api_url = 'http://127.0.0.1:8000'


@app.route('/')
@app.route('/product')
def index():
    response = requests.get(api_url + '/product')
    result = response.json()
    return render_template('index.html', consoles=result['data'])


@app.route('/product/<path:id>')
def console(id):
    response = requests.get(api_url + '/product/' + id)
    result = response.json()['data']
    return render_template('console.html',
                           console_name=result['product_name'],
                           console_price=result['price'],
                           console_sell=result['stock'])


if __name__ == '__main__':
    app.run(debug=True)
