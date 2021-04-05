from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/fortune_results', methods=['GET', 'POST'])
def fortune_results():
    users_favorite_city = request.args.get('city')
    return render_template('fortune_results.html', users_favorite_city=users_favorite_city)
