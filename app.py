from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

# Open the JSON file with api key
with open('api_key.json', 'r') as file:
    api_key = json.load(file)

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = api_key["api_key"]
WEATHER_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Please enter a city name.")
    
    try:
        response = requests.get(WEATHER_URL, params={'key': API_KEY, 'q': city})
        data = response.json()

        if 'error' in data:
            return render_template('index.html', error=data['error']['message'])

        weather_data = {
            'city': data['location']['name'],
            'temperature': data['current']['temp_c'],
            'description': data['current']['condition']['text'],
            'icon': data['current']['condition']['icon']
        }

    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")
    
    return render_template('index.html', weather=weather_data)


if __name__ == '__main__':
    app.run(debug=True)