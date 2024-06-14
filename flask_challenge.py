from flask import Flask, request, jsonify

app = Flask(__name__)
sensor_data_list = []

@app.route('/sensor/data', methods=['POST'])
def sensor_data():
  # Get the data from the request
  data = request.get_json()
  temperature = data['temperature']
  humidity = data['humidity']
  timestamp = data['timestamp']

  # store the sensor data
  sensor_data_list.append({'temperature': temperature, 'humidity': humidity, 'timestamp': timestamp})

  # Response message
  response = {'message': 'Data received successfully!'}

  # Return the response
  return jsonify(response)

@app.route('/sensor/data', methods=['GET'])
def get_sensor_data():
  # Get the sensor data from the dummy list
  print(sensor_data_list)

  # Return the sensor data
  return jsonify(sensor_data_list)

if __name__ == '__main__':
  app.run(debug=True)
