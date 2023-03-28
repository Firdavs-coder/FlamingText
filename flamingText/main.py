import requests
from urllib.parse import urlencode
from constants import url


class FlamingText:
    def __init__(self, **kwargs):
        self._url = url
        self._kwargs = kwargs

    def _generateParams(self):
        if len(self._kwargs) == 0:
            return ""
        return "&"+urlencode(dict(self._kwargs))

    def _generateURL(self):
        return self._url + self._generateParams()

    def process(self):
        url = self._generateURL()
        response = requests.get(url)
        return response


if __name__ == "__main__":
    obj = FlamingText(text="Firdavs", script="fluffy-logo")
    print(obj.process().text)
