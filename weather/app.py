#!/usr/bin/python3


from api import WeatherAPI
import database
def main(lat,log):
	weather_object = WeatherAPI()
	print ('API call initilized.')
	weather_data = weather_object.get_weather(lat,log)
	print(weather_data)
	print ('Weather information fetched.')
	database.insert_into_weather_data(weather_data)


if __name__ == '__main__':
	main(9.0950,76.4925)


