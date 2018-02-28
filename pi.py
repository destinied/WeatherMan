#!/usr/bin/env python
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('WeatherStation.json' , scope)

gc = gspread.authorize(credentials)

wks = gc.open ("DHT Humidity Logs").sheet1
