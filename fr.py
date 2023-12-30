import json
import pandas as pd
import requests


class FlightDataRetriever:
    def __init__(self, api_endpoint, headers):
        self.api_endpoint = api_endpoint
        self.headers = headers

    def retrieve_flight_data(self):
        response = requests.get(self.api_endpoint, headers=self.headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        json_data = json.loads(response.text)
        flight_data = pd.DataFrame(json_data.get('data', []))
        flight_data.set_index('flight_id', inplace=True)

        return flight_data


# Usage
api_endpoint = "https://www.flightradar24.com/flights/most-tracked"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}

flight_data_retriever = FlightDataRetriever(api_endpoint, headers)
flight_data = flight_data_retriever.retrieve_flight_data()
