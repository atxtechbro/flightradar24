import json
import pandas as pd
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}

api_endpoint = "https://www.flightradar24.com/flights/most-tracked"
response = requests.get(api_endpoint, headers=headers)

json_data = json.loads(response.text)
flight_data = pd.DataFrame(json_data['data'])
flight_data.set_index('flight_id', inplace=True)
