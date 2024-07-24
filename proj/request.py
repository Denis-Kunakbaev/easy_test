import requests


class EasyTest:
    url = 'https://jsonplaceholder.typicode.com/posts'

    def request(self):
        response = requests.get(self.url)
        return response
