import requests
import json

def get_weather(city: str) -> str:
    # Define the API endpoint and the key
    api_key = '677f8bbdf8e34cd0b1e95337240911'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    try:
        # Send the GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the required data (temperature and weather condition)
            location = data['location']['name']
            temperature = data['current']['temp_c'] 
            weather_condition = data['current']['condition']['text']

            
            # Return the weather data as JSON
            return json.dumps({"city": location, "weather": weather_condition, "temperature": temperature})

        else:
            return json.dumps({"error": "Unable to fetch weather data", "status_code": response.status_code})
    
    except Exception as e:
        return json.dumps({"error": f"Error: {str(e)}"})    

if __name__ == "__main__":
    get_weather(city)