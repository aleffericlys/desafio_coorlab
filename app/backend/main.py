from flask import Flask, request, jsonify
from flask_cors import CORS
import json

App = Flask('transport')
App.config.from_object(__name__)

CORS(App)
with open('app/backend/data.json', 'r') as file:
	data = json.load(file)

data = data['transport']

@App.route('/transport', methods=['GET'])
def transport():
	return data

@App.route('/transport/<city>', methods=['GET'])
def transport_id(city):
	result = []
	for item in data:
		if item['city'] == city:
			result.append(item)

	if result == []:
		return 'Not found', 404
	
	return jsonify(result)

@App.route('/transport_cityes', methods=['GET'])
def transport_city():
	result = []
	for item in data:
		if item['city'] not in result:
			result.append(item['city'])
	return jsonify(result)


if __name__ == '__main__':
	App.run(debug=True, port=3000)