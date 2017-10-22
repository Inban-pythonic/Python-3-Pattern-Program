import requests
city=input("Enter the City Name to Know Weather:")
url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=14692cdd4711f041878eb59564ef8b75"
data=requests.get(url)
read=data.json()
print("City Name  : {}".format(read['name']))
print("Country    : {}".format(read['sys']['country']))
print("Tempature  : {}F".format(read['main']['temp']))
print("Humidity   : {}%".format(read['main']['humidity']))
print("Pressure   : {}hpa".format(read['main']['pressure']))
print("Wind Speed : {}m/s".format(read['wind']['speed']))
print("Description: {}".format(read['weather'][0]['description']))




how do attach above 3rd line degree celcius.. pls help ..   
# Python Program to convert temperature in fahrenheit to celsius 

# change this value for a different result
fahrenheit = 99.5

# calculate celsius
celsius = (fahrenheit - 32) / 1.8
#print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit,celsius))

