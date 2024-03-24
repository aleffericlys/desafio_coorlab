from flask import Flask, request, jsonify
from flask_cors import CORS
import json

App = Flask('transport')
App.config.from_object(__name__)

CORS(App)

# with open('app/backend/data.json', 'r') as file:

with open('data.json', 'r') as file:
	data = json.load(file)

data = data['transport']

@App.route('/transport', methods=['GET'])
def transport():
	return data


def find_city(city):
	result = []
	for item in data:
		if item['city'] == city:
			result.append(item)

	return result



def find_cheapest(city):
	routes = find_city(city)
	if len(routes) == 0:
		return []
	else:
		cheapest = routes[0]
		for route in routes:
			if float(route['price_econ'].replace("R$ ", '')) < float(cheapest['price_econ'].replace("R$ ", '')):
				cheapest = route
		return cheapest

def find_fastest(city):
	routes = find_city(city)
	if len(routes) == 0:
		return []
	else:
		fastest = routes[0]
		for route in routes:
			if int(route['duration'].replace('h', '')) < int(fastest['duration'].replace('h', '')):
				fastest = route 
		return fastest

@App.route('/transport/<city>', methods=['GET'])
def transport_id(city):
	result = []
	fastest = find_fastest(city)
	cheapest = find_cheapest(city)

	if fastest != []:
		result.append(fastest) 
	
	if cheapest != []:
		if cheapest != fastest:
			result.append(cheapest)
	
	if result == []:
		return 'Not found', 404
	else:
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


