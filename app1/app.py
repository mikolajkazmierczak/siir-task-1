from flask import Flask
from flask_restful import Resource, Api, reqparse

import datetime, os

app = Flask(__name__)
api = Api(app)

class Time(Resource):
  def get(self):
    time = datetime.datetime.utcnow()

    print('\nReceiving GET request...')
    parser = reqparse.RequestParser()
    parser.add_argument('tz')
    args = parser.parse_args()
    print(args)

    hours_offset = args['tz']
    if hours_offset:
      # add or subtract hours from time in the current timezone
      # (typing a '+' before the number is irrelevant because maths)
      # (typing a '-' before the number will make it negative)
      time = time + datetime.timedelta(hours=int(hours_offset))
    time = time.time().replace(microsecond=0)

    print('Returning JSON data...')
    return {'time': str(time)}

  def post(self):
    print('\nReceiving POST request...')
    parser = reqparse.RequestParser()
    parser.add_argument('students', type=int, action='append')
    parser.add_argument('received_time')
    args = parser.parse_args()
    print(args)

    print('Writing received data to file...')
    path = './data'
    listdir = os.listdir(path)
    if len(listdir) >= 10: # spam check
      os.remove(f'{path}/{listdir[0]}')
    d = datetime.datetime.now()
    file_name = f'data-{d.day}-{d.month}-{d.year}-{d.hour}-{d.minute}-{d.second}'
    file_json = open(f'{path}/{file_name}.json', 'w+')
    file_json.write( str(args).replace("'",'"') )
    file_json.close()

api.add_resource(Time, '/time')

if __name__ == '__main__':
  app.run(debug=True)