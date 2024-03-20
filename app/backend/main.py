from flask import Flask, request, jsonify
import json

App = Flask('transport')

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
			pass
	
	if result == []:
		return 'Not found', 404
	return jsonify(item)

@App.route('/transport_cityes', methods=['GET'])
def transport_city():
	result = []
	for item in data:
		if item['city'] not in result:
			result.append(item['city'])
	return jsonify(result)


App.run(port=3000)