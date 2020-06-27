from tkinter import * 
from PIL import ImageTk,Image
import requests 
import json


root = Tk(className = 'Weather App')
root.iconbitmap('image/icon.ico')

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94027&distance=5&API_KEY=6438B5CF-9E4B-4BD0-9F8E-5DB1E46B6624


try:
	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94027&distance=5&API_KEY=6438B5CF-9E4B-4BD0-9F8E-5DB1E46B6624")
	api = json.loads(api_request.content)
	city = api[0]['ReportingArea']
	quality = api[0]['AQI']
	category = api[0]['Category']['Name']
	
	if category == "Good":
		weather_color = "Green"
	elif category == "Moderate":
		weather_color == "#ffff00"
	elif category == "Unhealthy for Sensitive Groups (USG)":
		weather_color == "#ff7e00"
	elif category == "Unhealthy":
		weather_color == "#ff0000"
	elif category == "Very Unhealthy":
		weather_color == "#99004c"
	elif category == "Hazardous":
		weather_color == "#7e0023"

	


	myLabel = Label(root, text = city + " Air Quality " + str(quality) + " "+category, font= ("Halvetica", "30"), background = weather_color).pack()

except Exception as e:
	api = "Error"


root.mainloop()



