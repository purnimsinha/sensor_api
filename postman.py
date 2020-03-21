import requests

url = 'http://127.0.0.1:5000/sensor/api/V1.0/data'
myobj = {"sensor_data": "1", "data_desc": "on the light python"}



y = requests.post(url,data=myobj)

#x = requests.get(url)

print(y.text)