import requests, os, time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")


#fetch with retry function
def fetch_with_retry(url, params=None, mx_retries=3, delay=2):
    for attempt in range(1 , mx_retries + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                wait = int(response.headers.get("Retry-After", delay))
                print(f'rate limit hit, retrying after {wait} seconds...')
                time.sleep(wait)

            elif response.status_code == 500:

                print(f'server error, retrying after {delay} seconds...')
                time.sleep(delay)

            else:
                print(f"Error: {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            print(f"Request timed out on attempt {attempt}. Retrying...")
            time.sleep(delay)

        # except requests.exceptions.ConnectionError:
        #     print("No internet connection. Please check your connection and try again.")
        #     return None

    print("All retries exhausted. Failed to fetch data.")
    return None
            





##########################################################

# call the function
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "hourly": "temperature_2m",
    "current_weather": True
}
data = fetch_with_retry(url, params=params)

if data:
    print(data["current_weather"])




##########################################################



import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# Get request weather for Rawalpindi
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Rawalpindi",
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params, timeout=10)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Description: {data['weather'][0]['description']}")
else:
    print(f"Error fetching weather data: {response.status_code}")



#Post request - your name and bio
post_url = 'https://jsonplaceholder.typicode.com/posts'


payload = {
    "title": "Ahmad Karim",
    'body': "I am a software developer with a passion for learning new technologies and building innovative solutions.",
    'userId': 1
}

post_response = requests.post(post_url, json=payload, timeout=10)

if post_response.status_code == 201:
    created_post = post_response.json()
    print("\n=====POst request=====")
    print(f"Post Id: {created_post['id']}")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
   





