_author = 'Ruthesh'
import pymysql as MySQLdb

#import MySQLdb
from credentails import DB_HOST,DB_USER_NAME,DB_DATABASE_NAME,DB_PASSWORD

class DatabaseOperation:
	"""
	It's used to all kind of database operations.
	"""

	def __init__(self):
		self.conn = MySQLdb.connect(host=DB_HOST,
							user=DB_USER_NAME,
							passwd=DB_PASSWORD,
							db=DB_DATABASE_NAME)
		self.cursor = self.conn.cursor()
		self.key_order = ['summary','precipIntensity','precipIntensityError','precipProbability','precipType','humidity',
			'temperature','apparentTemperature','windSpeed','windGust','windBearing','cloudCover','visibility']

	def insert_into_weather_data(self,weather_data):
		raw_query = """INSERT INTO weather_data 
						(summary,precipIntensity,precipIntensityError,precipProbability,
						precipType,humidity,temperature,apparentTemperature,windSpeed,
						windGust,windBearing,cloudCover,visibility)
						values 
						(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		try:
			self.cursor.execute(raw_query,(weather_data.get(key) for key in self.key_order))
			self.conn.commit()
			print ('Weather data inserted in database.')
		except:
			self.conn.rollback()
			print ('Database insertion failed.')