import requests, json, os
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()

# TODO: Try with all available API from .env
END_POINT = os.getenv("API_1")

# 1. API response via urlopen
# Fetch data from the API endpoint using `urlopen`
# This approach uses the built-in `urllib` library.
# - `urlopen(END_POINT)` opens a connection to the specified URL.
# - The response is then read using `api_response_v1.read()`.
# - Finally, the response is decoded as JSON using `json.loads()`.
api_response_v1 = urlopen(END_POINT)
api_response_v1 = json.loads(api_response_v1.read())

# 2. API response via requests
# Fetch data from the API endpoint using `requests` library
# This approach is generally considered more modern and flexible.
# - `requests.get(END_POINT)` sends a GET request to the URL.
# - The response object directly contains the decoded data.
api_response_v2 = requests.get(END_POINT)
api_response_v3 = eval(api_response_v2.text)

# TODO: Check the data type
print()
print(api_response_v1)
print()
print(api_response_v2.text)
print()
print(api_response_v3)
print()
print(type(api_response_v1))
print()
print(type(api_response_v2.text))
print()
print(type(api_response_v3))
print()