from bs4 import BeautifulSoup
import requests

page = requests.get('https://openweathermap.org/city/2803138')
soup = BeautifulSoup()