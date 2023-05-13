import json
import requests


def get_input():
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        return lat, lon
    except ValueError as error:
        print("Invalid input:", error)
        return None, None


def run(lat, lon):
    try:
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
        querystring = {
            "lat": str(lat),
            "lon": str(lon)
        }

        headers = {
            # -- ENTER YOUR API KEY FROM RAPID API HERE --
            "X-RapidAPI-Key": "ENTER_YOUR_API_KEY",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = json.loads(response.text)

        # Process the data or perform desired actions
        print(data)

    except Exception as error:
        print("An error occurred:", error)


# -- RUN UNTIL PROGRAM IS CLOSED --
while True:
    lat, lon = get_input()
    if lat is None:
        continue
    run(lat, lon)
