# get the results from weather api
# and return the results in json format

import requests
import json

# get the results from weather api
if  __name__ == '__main__':
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=5b4d4c4f7f4f4c4f4c4f4c4f4c4f4c4f'
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))



