from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = '43c4ccb9a303913fc24b00bc46832b3e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)