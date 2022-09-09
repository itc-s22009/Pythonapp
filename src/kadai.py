import requests
import pandas as pd
from dotenv import load_dotenv
import os
import csv

load_dotenv('.env')
REQUEST_URL = 'https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426'

params={
    'format': 'json',
    'largeClassCode': 'japan',
    'middleClassCode': input('都道府県をローマ字で： '),
    'smallClassCode': input('市区町村をローマ字で： '),
    'detailClassCode': input('細かい地域： '),
    'applicationId': os.environ.get('APP_ID')
    }
response = requests.get(REQUEST_URL, params)
result = response.json()


df = pd.DataFrame()
hotels = result['hotels']
for i, hotel in enumerate(hotels):
    hotel_info = hotel['hotel'][0]['hotelBasicInfo']
    _df = pd.DataFrame(hotel_info, index=[i])
    df = df.append(_df)
    
view = df[['hotelName','reviewAverage',]]#.to_csv('hotel.csv',index=False)

print(view)



