_author = 'Ruthesh'
import pymysql as MySQLdb

#import MySQLdb
#from credentails import DB_HOST,DB_USER_NAME,DB_DATABASE_NAME,DB_PASSWORD

		

def insert_into_weather_data(weather_data):
	conn = MySQLdb.connect(host="localhost",user="admin",passwd="admin",db="krishi")
	cursor = conn.cursor()
	key_order = ['summary','precipIntensity','precipIntensityError','precipProbability','precipType','humidity','temperature','apparentTemperature','windSpeed','windGust','windBearing','cloudCover','visibility']
	raw_query = """INSERT INTO weatherlog(summary,precipIntensity,precipProbability,precipType,humidity,temperature,apparentTemperature,windSpeed,windGust,windBearing,cloudCover,visibility)
	values(%(summary)s,%(precipIntensity)s,%(precipProbability)s,%(precipType)s,%(humidity)s,%(temperature)s,%(apparentTemperature)s,%(windSpeed)s,%(windGust)s,%(windBearing)s,%(cloudCover)s,%(visibility)s)"""
	cursor.execute(raw_query,weather_data)
	conn.commit()
	conn.close()
