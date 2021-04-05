from flask import Flask, render_template, request

import requests

app = Flask(__name__)

weather_url = "https://api.openweathermap.org/data/2.5/weather"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/fortune_results', methods=['GET', 'POST'])
def fortune_results():
    users_favorite_city = request.args.get('city')
    return render_template('fortune_results.html', users_favorite_city=users_favorite_city)


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    return render_template('weather_form.html')


@app.route('/weather_results', methods=['GET', 'POST'])
def weather_results():
    users_city = request.args.get('weatherCity')

    params = {
        'q': users_city,
        'appid': '2608f679d4594364525f6c6cc2246c79'
    }

    response = requests.get(weather_url, params=params)
    results = response.json()

    temp = results['main']['temp']

    return render_template('weather_results.html', users_city=users_city, temp=temp)
