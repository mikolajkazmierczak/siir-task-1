import paho.mqtt.client as mqtt
import requests, time, json

def on_message(client, userdata, message):
  INDEX_NUMBERS = [254287, 254000]
  time = json.loads(message.payload.decode('utf-8'))
  data = {
    'students': INDEX_NUMBERS,
    'received_time': time['time']
  }
  print(f'Sending: {data} to the HTTP server.')
  request = requests.post(f'http://localhost:5000/time', data=data)

client = mqtt.Client('TIME_SUBSCRIBER')
client.on_message = on_message
client.connect('test.mosquitto.org')

client.loop_start()
while True:
  client.subscribe('time/timezone')
  time.sleep(5)
client.loop_stop()

client.disconnect()
