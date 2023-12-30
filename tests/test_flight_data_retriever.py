import unittest
from unittest.mock import MagicMock, patch

from src.flight_data_retriever import FlightDataRetriever


class TestFlightDataRetriever(unittest.TestCase):
    def setUp(self):
        self.api_endpoint = ("https://www.flightradar24.com/"
                             "flights/most-tracked")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'
        }

    @patch('flight_data_retriever.requests.get')
    def test_retrieve_flight_data(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = (
            '{"data": [{"flight_id": "123", "callsign": "ABC"}]}'
        )
        mock_get.return_value = mock_response

        # Create an instance of the FlightDataRetriever
        flight_data_retriever = FlightDataRetriever(
            self.api_endpoint, self.headers
        )

        # Call the method under test
        flight_data = flight_data_retriever.retrieve_flight_data()

        # Assert the expected behavior
        self.assertEqual(flight_data.iloc[0]['flight_id'], '123')
        self.assertEqual(flight_data.iloc[0]['callsign'], 'ABC')


if __name__ == '__main__':
    unittest.main()
