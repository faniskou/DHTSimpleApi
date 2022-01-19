# first you must run the above packages
# pip3 install Adafruit_Python_DHT
# pip3 install Flask
# pip3 install Flask-RESTful

try:
    from flask import Flask
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask import request
    import time
    import datetime
    import json
    import Adafruit_DHT
    import threading


    print("All modules loaded ")
except Exception as e:
    print("Error: {}".format(e))

app = Flask(__name__)
api = Api(app)

# Choose your GPIOx port
pin = 3
# Choose your sensor Adafruit_DHT.AM2302 , Adafruit_DHT.DHT11 , Adafruit_DHT.DHT22
sensor = Adafruit_DHT.AM2302

humidity_save = 0
temperature_save = 0

class threadClass:

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                       # Daemonize thread
        thread.start()                             # Start the execution

    def run(self):
        global humidity_save
        global temperature_save

        while True:
          humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

          if humidity is not None and temperature is not None:
              humidity_save = humidity
              temperature_save = temperature
              print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
          else:
              print("Failed to retrieve data from humidity sensor")




class Sensors(object):

    def __init__(self):
        pass

    def get(self):

        global humidity_save
        global temperature_save
        return{
                'temperature':temperature_save,
                "humidity":humidity_save
        }


class Controller(Resource):
    def __init__(self):
        pass

    def get(self):
        helper = Sensors()
        return helper.get()


api.add_resource(Controller, "/")

#  No port is assigned so will propably run on 5000
if __name__ == "__main__":
    try:
        begin = threadClass()
    except:
        abort(500)
    app.run(host='0.0.0.0')
