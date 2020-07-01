from datetime import datetime, timedelta

# def roundTime(dt = None, roundTo = 60):
	"""Purpose: Returns a rounded value of a datetime object
	to a timedelta object.
	"""
	

	# if(dt == None): 
	# 	dt = datetime.datetime.now()
	# seconds = (dt.replace(tzinfo = None) - dt.min).seconds
	# rounding = (seconds + roundTo/2) // roundTo * roundTo
	# return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)

if __name__ == "__main__":
	# print(roundTime(datetime.datetime(2012, 12, 31, 23, 44, 59, 1234), roundTo = 60*60))
	f = datetime.now() + timedelta(days = 10)