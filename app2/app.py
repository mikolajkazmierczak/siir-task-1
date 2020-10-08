import paho.mqtt.client as mqtt
import requests, time

TIMEZONE = '+3'

client = mqtt.Client('TIME_PUBLISHER')
client.connect('test.mosquitto.org')

client.loop_start()
while True:
  request = requests.get(f'http://localhost:5000/time?tz={TIMEZONE}')
  print(request.text)
  client.publish('time/timezone', request.text)
  time.sleep(5)
client.loop_stop()

client.disconnect()