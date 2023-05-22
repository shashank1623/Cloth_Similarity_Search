import requests
import json

# Define the URL for the POST request
url = 'http://13.233.174.242:8060/compute_similarity'

# Define the JSON payload
payload = {
    "input_text": "mini shorts",
    "N": 5
}

# Send the POST request with the JSON payload
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Print the response content
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
