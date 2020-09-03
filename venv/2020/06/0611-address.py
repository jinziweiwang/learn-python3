import json

import requests

class Adress(object):
    def __init__(self,address=None,location=None):
        self._address = address
        selt._location = location
        self._base_url = "http://api.map.baidu.com"