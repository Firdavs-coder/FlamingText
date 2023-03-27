import requests
from constants import url


class FlamingText:
    def __init__(self):
        self._url = url

    def process(self):
        response = requests.post(self._url)
        return response


if __name__ == "__main__":
    obj = FlamingText()
    print(obj.process())
