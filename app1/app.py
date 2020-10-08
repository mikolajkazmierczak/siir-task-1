from flask import Flask
from flask_restful import Resource, Api, reqparse

import datetime

app = Flask(__name__)
api = Api(app)

class Time(Resource):
  def get(self):
    time = datetime.datetime.now()
    parser = reqparse.RequestParser()
    parser.add_argument('tz')
    args = parser.parse_args()
    hours_offset = args['tz']
    if hours_offset:
      # add or subtract hours from time in the current timezone
      # (typing a '+' before the number is irrelevant because maths)
      # (typing a '-' before the number will make it negative)
      time = datetime.datetime.now() + datetime.timedelta(hours=int(hours_offset))
    time = time.time().replace(microsecond=0)
    return {'time': str(time)}

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('students')
    parser.add_argument('received_time')
    args = parser.parse_args()
    print(args)
    students = args['students']
    received_time = args['received_time']
    print(students)
    print(received_time)

api.add_resource(Time, '/time')

if __name__ == '__main__':
  app.run(debug=True)