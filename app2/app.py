import paho.mqtt.client as mqtt
import requests, time

print('Connecting to an MQTT client...')

client = mqtt.Client('TIME_PUBLISHER')
client.connect('test.mosquitto.org')

client.loop_start()
while True:
  TIMEZONE = '+3'
  print('\nGetting JSON data from a URL...')
  request = requests.get(f'http://localhost:5000/time?tz={TIMEZONE}')
  data = request.text.strip()
  print(data)
  print('Publishing JSON string data to the MQTT client...')
  client.publish('time/timezone/qRfgP1o', data)
  time.sleep(5)
client.loop_stop()

client.disconnect()