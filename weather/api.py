_author = 'Ruthesh'

from credentails import API_TOKEN
import requests

class WeatherAPI:
	"""
	It's an api use to collect all weather informatoion.
	"""

	def __init__(self):
		self.URL = 'https://api.darksky.net/forecast/'
		self.url_to_fetch = self.URL+'{api_key}/{latitude},{longitude}'

	def get_weather(self,latitude,longitude):
		keys_to_fetch = {'api_key':API_TOKEN,
							'latitude':latitude,
							'longitude':longitude}
		res = requests.get(self.url_to_fetch.format(**keys_to_fetch))
		current_data = res.json().get('currently')
		if current_data:
			data = {'summary':current_data.get('summary',''),
					'precipIntensity':current_data.get('precipIntensity'),
					'precipIntensityError':current_data.get('precipIntensityError'),
					'precipProbability':current_data.get('precipProbability'),
					'precipType':current_data.get('precipType',''),
					'humidity':current_data.get('humidity'),
					'temperature':current_data.get('temperature'),
					'apparentTemperature':current_data.get('apparentTemperature'),
					'windSpeed':current_data.get('windSpeed'),
					'windGust':current_data.get('windGust'),
					'windBearing':current_data.get('windBearing'),
					'cloudCover':current_data.get('cloudCover'),
					'visibility':current_data.get('visibility')
					}
			return data
		else:
			return {'Error':'Something went wrong'}
