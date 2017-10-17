# my app id : 55caddfec6f90b2b717bb37ceab8abb0
"""
	Name 		  : Raghav Dev Kukreti
	Roll No 	  : 2017082
	Section-Group : B1

"""
import urllib.request
import datetime

# function to get weather response
def weather_response(location, API_key):
	with urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=' + location + '&APPID='+API_key) as response:
		resp = response.read()
	return resp.decode("utf-8") 

json_parsed = weather_response('Delhi', '55caddfec6f90b2b717bb37ceab8abb0')

# function to check for valid response 
def has_error(location, json):
	# True if input and response city are not matched
	if location in str(json) :
		return False
	else :
		return True
# function to get attributes on nth day
# time is of the format 00:00:00
def get_temperature (json, t, n=0):
	#get todays date
	#find n
	#loop through the string, increment i till i==n and take that block of JSON
	# time formatted like this :09, 12, 15, 18, 21, 00(next day)
	date = str(datetime.date.today())
	json_converted = str(json)
	# format of dt_txt = date time
	dt_txt_index = json_converted.find(date + " " + str(t))
	mate = json_converted.rfind('"temp":', 0, dt_txt_index)
	comma_index = json_converted.find(",", mate)
	mate = mate + 7
	return (float(json_converted[mate:comma_index]))

def get_humidity(json,t,n=0):
	# write your code 
	date = str(datetime.date.today())
	json_converted = str(json)
	# format of dt_txt = date time
	dt_txt_index = json_converted.find(date + " " + str(t))
	mate = json_converted.rfind('"humidity":', 0, dt_txt_index)
	comma_index = json_converted.find(",", mate)
	mate = mate + 11
	return (int(json_converted[mate:comma_index]))

def get_pressure(json, t, n=0):
	date = str(datetime.date.today())
	json_converted = str(json)
	# format of dt_txt = date time
	dt_txt_index = json_converted.find(date + " " + str(t))
	mate = json_converted.rfind('"pressure":', 0, dt_txt_index)
	comma_index = json_converted.find(",", mate)
	mate = mate + 11
	return (float(json_converted[mate:comma_index]))

def get_wind(json, t,n=0):
	date = str(datetime.date.today())
	json_converted = str(json)
	# format of dt_txt = date time
	dt_txt_index = json_converted.find(date + " " + str(t))
	mate = json_converted.rfind('"speed":', 0, dt_txt_index)
	comma_index = json_converted.find(",", mate)
	mate = mate + 8
	return (float(json_converted[mate:comma_index]))

def get_sealevel(json, t, n=0):
	date = str(datetime.date.today())
	json_converted = str(json)
	# format of dt_txt = date time
	dt_txt_index = json_converted.find(date + " " + str(t))
	mate = json_converted.rfind('"sea_level":', 0, dt_txt_index)
	comma_index = json_converted.find(",", mate)
	mate = mate + 12
	return (float(json_converted[mate:comma_index]))


print(weather_response("Delhi", "55caddfec6f90b2b717bb37ceab8abb0"))
print(has_error("Del",json_parsed))
# print(datetime.date.today())
lol = input("Enter number of days: ")
time = input("Enter time: ")
print(get_temperature (json_parsed,int(lol), time))
print(get_humidity (json_parsed,int(lol), time))
print(get_pressure (json_parsed,int(lol), time))
print(get_wind (json_parsed,int(lol), time))
print(get_sealevel (json_parsed,int(lol), time))

