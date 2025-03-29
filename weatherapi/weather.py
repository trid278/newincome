from flask import Flask, request, jsonify
import requests
from waitress import serve
import os         

app = Flask(__name__)

# Replace with your actual WeatherAPI key.
WEATHER_API_KEY = "1cd079e56c6242d581060254252903"

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Retrieves weather data for an Indian city using WeatherAPI.
    Defaults to Delhi if no city is provided in the query string.
    """
    city = request.args.get('city', 'Delhi')
    
    # Build the WeatherAPI endpoint for current weather.
    # 'q={city},India' ensures the location is in India.
    # 'aqi=no' is optional, disables Air Quality Index data for simplicity.
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city},India&aqi=no"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information from the API response
        current_weather = {
            "location": data.get("location", {}).get("name"),
            "region": data.get("location", {}).get("region"),
            "country": data.get("location", {}).get("country"),
            "temperature_celsius": data.get("current", {}).get("temp_c"),
            "condition": data.get("current", {}).get("condition", {}).get("text"),
            "icon": data.get("current", {}).get("condition", {}).get("icon"),
        }
        return jsonify(current_weather), 200
    else:
        # If the API call fails, return an error message.
        return jsonify({"error": "Weather data not found"}), response.status_code
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Default port for local testing
    serve(app, host="0.0.0.0", port=port)
    

#if __name__ == '__main__':
    # For local development only; remove debug=True in production.
    #app.run(debug=True)

