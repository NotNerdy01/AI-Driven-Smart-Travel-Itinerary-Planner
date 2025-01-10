# import requests

# url = "https://api.foursquare.com/v3/places/search"

# params = {
#   	"query": "tourist",
#   	"near": "Mumbai",
#   	"open_now": "true",
#   	"sort":"DISTANCE"
# }

# headers = {
#     "Accept": "application/json",
#     "Authorization": "fsq3tiwckB5KfwtTck0np5WTH0XRLKcfUD3ilr7tzXVIt7k="
# }

# response = requests.request("GET", url, params=params, headers=headers)
# list_place = [i['name'] for i in response.json()["results"]]

# for i in list_place:
#     print(i)

import requests
import json

def get_tourist_places(city: str) -> str:
    # Define the Foursquare API endpoint and API key
    url = "https://api.foursquare.com/v3/places/search"
    api_key = "fsq3tiwckB5KfwtTck0np5WTH0XRLKcfUD3ilr7tzXVIt7k="
    
    # Define parameters for the request
    params = {
        "query": "tourist",
        "near": city,
        "open_now": "true",
        "sort": "DISTANCE"
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"fsq3tiwckB5KfwtTck0np5WTH0XRLKcfUD3ilr7tzXVIt7k="
    }

    try:
        # Send the GET request to the Foursquare API
        response = requests.get(url, params=params, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the names of the tourist places
            places = [place['name'] for place in data["results"]]

            # Return the list of tourist places as JSON
            return json.dumps({"city": city, "tourist_places": places})

        else:
            return json.dumps({"error": "Unable to fetch tourist places data", "status_code": response.status_code})

    except Exception as e:
        return json.dumps({"error": f"Error: {str(e)}"})

if __name__ == "__main__":
    get_tourist_places(city)
