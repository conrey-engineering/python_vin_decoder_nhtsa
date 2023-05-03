import requests
import json

class Vin():
    VIN = None

    def _search(self):
        url = 'https://vpic.nhtsa.dot.gov/api//vehicles/DecodeVinValues/{}?format=json'.format(self.VIN)
        resp = requests.get(url)
        data = resp.json()
        return data['Results']

    def __init__(self, vin):
        self.VIN = vin
        data = self._search()
        for k, v in data[0].items():
            if v == '':
                v = None
            setattr(self, k, v)

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)