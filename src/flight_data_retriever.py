import json
import pandas as pd
import logging

import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class FlightDataRetriever:
    def __init__(self, api_endpoint, headers):
        self.api_endpoint = api_endpoint
        self.headers = headers

    def retrieve_flight_data(self):
        logging.info('Sending request to %s', self.api_endpoint)
        try:
            response = requests.get(
                self.api_endpoint,
                headers=self.headers,
                timeout=5
            )
        except requests.Timeout:
            logging.error('Request to %s timed out', self.api_endpoint)
            return None

        response.raise_for_status()  # Raise HTTPError for bad responses

        json_data = json.loads(response.text)
        flight_data = pd.DataFrame(json_data.get('data', []))
        flight_data.set_index('flight_id', inplace=True)

        logging.info('Successfully retrieved flight data')
        return flight_data

    def analyze_flight_data(self):
        flight_data = self.retrieve_flight_data()

        most_common_departure_city = flight_data['from_city'].mode().get(0)
        most_common_arrival_city = flight_data['to_city'].mode().get(0)

        logging.info("The most common departure city is: %s",
                     most_common_departure_city)
        logging.info("The most common arrival city is: %s",
                     most_common_arrival_city)


# Usage
api_endpoint = "https://www.flightradar24.com/flights/most-tracked"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}

flight_data_retriever = FlightDataRetriever(api_endpoint, headers)
flight_data_retriever.analyze_flight_data()
