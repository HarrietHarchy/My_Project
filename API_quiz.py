import requests

resp = requests.get("http://samples.openweathermap.org/pollution/v1/co/0.0,10.0/current.json?appid=b1b15e88fa797225412429c1c50c122a1")
print(resp.status_code)
print resp.json

for todo_item in resp.json():
	print(todo_item)

if resp.status_code !=200:

 	# this means something went wrong.
	
	# raise A_Error('{GET /https://developer.foursquare.com/}'.format(resp.status_code))
	pass
