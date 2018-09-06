# 1. Make your API Key
# 2. Python2/3 you can make API calls fetch data in json
# 3. Json try separate elements into variables

import requests
import re
import datetime


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=raw_api_dict.get('sys').get('sunrise'),
        sunset=raw_api_dict.get('sys').get('sunset'),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=raw_api_dict.get('dt'),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data



r = requests.get(url='http://api.openweathermap.org/data/2.5/forecast?q=bangalore&mode=json&units=metric&APPID=xxxxxxxxxxxxxxx')
json_data= r.json()
# print(json_data)
# print(json_data['list'][0]['dt_txt'])
list_items= json_data['list']
# print(list_items)

#02-07-2018



now = datetime.datetime.now()
# print(now)
today= now.day

#
list_indices = []
#
for items in list_items:
    matchObj = re.match(r"(\d+)-(\d+)-(\d+)",items['dt_txt'], re.M | re.I)
    # print(matchObj.group(3))
    list_indices.append(matchObj[3])
# print(list_indices)

#
# # print(list_indices[0])
#
# list.index(item)

# print(today)
for items in list_indices:
    if(int(items) == today+1):
        # print("yay")
        # print(items)
        index=list_indices.index(items)
        # print(index)
        break

# print(index)
# #
# print(list_items[index])

print(data_organizer(list_items[index]))



#
# for items in list_items:
#     print(items['dt_txt'])
#     # var=current date
#     # if(pattern comp var):
#     #     today=items
#     # elif(pattern comp var-1 ):
#     #   previous=items
#     # elif(pattern comp var+1)
#     #   tomorrow=items
# import tkinter
#
# m=tkinter.Tk(className='First window')
# m.mainloop()
#
# import datetime
# import json
# import urllib.request
# from tkinter import *
#
#
# def fetch_data():
#     city_name = city_entry.get()
#     data_output(data_organizer(data_fetch(url_builder(city_name))))
#
# def time_converter(time):
#     converted_time = datetime.datetime.fromtimestamp(
#         int(time)
#     ).strftime('%I:%M %p')
#     return converted_time
#
#
# def url_builder(city_name):
#     user_api = 'xxxxxxxxxxxxxxxxxx'  # Obtain yours form: http://openweathermap.org/
#     unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
#     api = 'http://api.openweathermap.org/data/2.5/weather?q='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz
#
#     full_api_url = api + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + user_api
#     return full_api_url
# # http://api.openweathermap.org/data/2.5/weather?id=1273294&mode=json&units=metric&APPID=xxxxxxxxxxxxxx
#
#
# def data_fetch(full_api_url):
#     url = urllib.request.urlopen(full_api_url)
#     output = url.read().decode('utf-8')
#     # print(output)
#     raw_api_dict = json.loads(output)
#     # print(raw_api_dict)
#     url.close()
#     return raw_api_dict
#
#
# def data_organizer(raw_api_dict):
#     data = dict(
#         city=raw_api_dict.get('name'),
#         country=raw_api_dict.get('sys').get('country'),
#         temp=raw_api_dict.get('main').get('temp'),
#         temp_max=raw_api_dict.get('main').get('temp_max'),
#         temp_min=raw_api_dict.get('main').get('temp_min'),
#         humidity=raw_api_dict.get('main').get('humidity'),
#         pressure=raw_api_dict.get('main').get('pressure'),
#         sky=raw_api_dict['weather'][0]['main'],
#         sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
#         sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
#         wind=raw_api_dict.get('wind').get('speed'),
#         wind_deg=raw_api_dict.get('deg'),
#         dt=time_converter(raw_api_dict.get('dt')),
#         cloudiness=raw_api_dict.get('clouds').get('all')
#     )
#     return data
#
#
# def data_output(data):
#
#
#     m_symbol = '\xb0' + 'C'
#     degree_sign = u'\N{DEGREE SIGN}'
#     # print('---------------------------------------')
#     # print('Current weather in: {}, {}:'.format(data['city'], data['country']))
#     # print(data['temp'], m_symbol, data['sky'])
#     # print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
#     # print('')
#     # print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
#     # print('Humidity: {}'.format(data['humidity']))
#     # print('Cloud: {}'.format(data['cloudiness']))
#     # print('Pressure: {}'.format(data['pressure']))
#     # print('Sunrise at: {}'.format(data['sunrise']))
#     # print('Sunset at: {}'.format(data['sunset']))
#     # print('')
#     # print('Last update from the server: {}'.format(data['dt']))
#     # print('---------------------------------------')
#     # print(data)
#
#     # print(data.get('city'))
#     city_lab= Label(m,text="City:")
#     city_lab.grid(row=5,column=0)
#
#     city_data.config(text=data['city'])
#     city_data.grid(row=5,column=1)
#
#     country_data.config(text=data['country'])
#     country_data.grid(row=5, column=2)
#
#     temp_max.config(text=str(data['temp_max'])+m_symbol)
#     temp_max.grid(row=6, column=1)
#
#     temp_min.config(text=str(data['temp_min'])+m_symbol)
#     temp_min.grid(row=6, column=2)
#
#
# try:
#     # city_name= input("Enter a city name:")
#     m = Tk(className='Weather Forecast')
#
#     city_label = Label(m,text="Enter a city: ")
#     city_label.grid(row=0,column=0)
#     city_entry = Entry(m)
#     city_entry.grid(row=0,column=1)
#
#
#     show = Button(m,text="Show", command=fetch_data)
#     show.grid(row=1, column=1)
#
#     city_data = Label(m)
#     country_data= Label(m)
#     temp_max = Label(m)
#     temp_min = Label(m)
#     # city_name = input("Enter a city name:")
#
#     m.mainloop()
# except IOError:
#     print('no internet')