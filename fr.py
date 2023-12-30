import json
import pandas as pd
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}

api_endpoint = "https://www.flightradar24.com/flights/most-tracked"
response = requests.get(api_endpoint, headers=headers)

# Log the API request status
logger.info(f"API request status code: {response.status_code}")

try:
    json_data = json.loads(response.text)
    flight_data = pd.DataFrame(json_data['data'])
    flight_data.set_index('flight_id', inplace=True)
    logger.info("Data loaded successfully")
except json.JSONDecodeError as e:
    logger.error(f"Error decoding JSON data: {e}")
except KeyError as e:
    logger.error(f"KeyError: {e}. Check the structure of the JSON response.")
    flight_data = pd.DataFrame()

# Log the number of rows and columns in the DataFrame
logger.info(f"Number of rows: {flight_data.shape[0]}, Number of columns: {flight_data.shape[1]}")
