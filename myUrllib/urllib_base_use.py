import requests
from bs4 import BeautifulSoup
class urllib_base_use:
    def __init__(self):
        pass

    def open_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())