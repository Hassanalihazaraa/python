from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")
print(items)
