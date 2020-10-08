import paho.mqtt.client as mqtt
import requests, time, json

def on_message(client, userdata, message):
  try:
    print(f'\nReceiving data from the MQTT client...')
    INDEX_NUMBERS = [254287, 254000]
    time = json.loads(message.payload.decode('utf-8'))
    data = {
      'students': INDEX_NUMBERS,
      'received_time': time['time']
    }
    print(f'Sending: {data} to the HTTP server...')
    request = requests.post(f'http://localhost:5000/time', data=data)
  except:
    print('An error occured...')

print('Connecting to an MQTT client...')

client = mqtt.Client('TIME_SUBSCRIBER')
client.on_message = on_message
client.connect('test.mosquitto.org')

client.loop_start()
while True:
  print('\nSubscribing to the MQTT topic...')
  client.subscribe('time/timezone/qRfgP1o')
  time.sleep(5)
client.loop_stop()

client.disconnect()
