import json

import pandas as pd
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.flightradar24.com/flights/most-tracked"
r = requests.get(url, headers=headers)

j = json.loads(r.text)
df = pd.DataFrame(j['data'])
df.set_index('flight_id')
