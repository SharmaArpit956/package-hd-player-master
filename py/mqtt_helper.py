import requests
import json

# Adafruit IO configuration
ADAFRUIT_IO_USERNAME = 'inventrepreneur'
ADAFRUIT_IO_KEY = '2a104ea34f614672aaea78f071963e3d'

# Adafruit IO base URL
ADAFRUIT_IO_URL = 'https://io.adafruit.com/api/v2/%s' % ADAFRUIT_IO_USERNAME

def send_data_to_adafruit_io(feed_key, value):
    url = '%s/feeds/%s/data' % (ADAFRUIT_IO_URL, feed_key)
    headers = {'Content-Type': 'application/json'}
    data = {'value': value}
    params = {'X-AIO-Key': ADAFRUIT_IO_KEY}

    response = requests.post(url, headers=headers, data=json.dumps(data), params=params)
    return response.status_code < 400

def get_data_from_adafruit_io(feed_key):
    url = '%s/feeds/%s/data/last' % (ADAFRUIT_IO_URL, feed_key)
    params = {'X-AIO-Key': ADAFRUIT_IO_KEY}

    response = requests.get(url, params=params)
    if response.status_code < 400:
        data = response.json()
        return data['value']
    return None

# print(send_data_to_adafruit_io('current-asset-name', "Costa 2"))
