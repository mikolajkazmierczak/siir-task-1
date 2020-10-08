from flask import Flask
from flask_restful import Resource, Api, reqparse

import datetime

app = Flask(__name__)
api = Api(app)

class Time(Resource):
  def get(self):
    print('\nReceiving GET request...')
    time = datetime.datetime.now()
    parser = reqparse.RequestParser()
    parser.add_argument('tz')
    args = parser.parse_args()
    print(args)
    hours_offset = args['tz']
    if hours_offset:
      # add or subtract hours from time in the current timezone
      # (typing a '+' before the number is irrelevant because maths)
      # (typing a '-' before the number will make it negative)
      time = datetime.datetime.now() + datetime.timedelta(hours=int(hours_offset))
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
    d = datetime.datetime.now()
    print('Writing received data to file...')
    file_name = f'data-{d.day}-{d.month}-{d.year}-{d.hour}-{d.minute}-{d.second}'
    file_json = open(f'data/{file_name}.json', 'w+')
    output_json_str = str(args).replace("'",'"')
    file_json.write(output_json_str)
    file_json.close()

api.add_resource(Time, '/time')

if __name__ == '__main__':
  app.run(debug=True)