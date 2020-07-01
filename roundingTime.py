from datetime import datetime

def roundTime(dt = None, roundTo = 60):
	"""Purpose: 
	"""
	if(dt == None): 
		dt = datetime.datetime.now()
	seconds = (dt.replace(tzinfo = None) - dt.min).seconds
	rounding = (seconds + roundTo/2) // roundTo * roundTo
	return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)

if __name__ == "__main__":
