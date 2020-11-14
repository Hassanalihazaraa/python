import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

period_names = [item.find(class_="period-name").get_text() for item in items]
short_desc = [item.find(class_="short-desc").get_text() for item in items]
temp = [item.find(class_="temp").get_text() for item in items]

weather_forecast = pd.DataFrame(
    {
        'period': period_names,
        'short_description': short_desc,
        'temperature': temp,
    }
)
# insert all data into csv file
weather_list.to_csv('weather.csv')

print(weather_list)
