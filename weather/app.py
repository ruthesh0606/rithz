_author = 'Ruthesh'

from api import WeatherAPI
from database import DatabaseOperation

def main(lat,log):
	weather_object = WeatherAPI()
	database_object = DatabaseOperation()
	print ('API call initilized.')
	weather_data = weather_object.get_weather(lat,log)
	print(weather_data)
	print ('Weather information fetched.')
	database_object.insert_into_weather_data(self,weather_data)
	database_object.conn.close()


if __name__ == '__main__':
	main(12.9716,77.5946)


