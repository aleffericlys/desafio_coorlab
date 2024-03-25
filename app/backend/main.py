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
	"""
	Search for all trips to a city

	Args:
		city (string): Codade que deseja buscar

	Returns:
		[] if not found any trip to the desired city,
		bject: have information like price, duration, city of destiny, types of seats. The object have the attributes: 

		"id"              <--- ID

    	"name"           <--- Name of company

    	"price_confort"  <--- value of trip in confort mode

    	"price_econ"     <--- value of trip in economic mode

    	"city"           <--- City of destiny

    	"duration"       <--- Duration of trip

    	"seat"           <--- seat (economic mode)

    	"bed"            <--- sleeper seats (confort mode)
	"""
	result = []
	for item in data:
		if item['city'] == city:
			result.append(item)

	return result



def find_cheapest(city):
	"""
	Search for the cheapest option for a city

	Args:
		city (string): Codade que deseja buscar

	Returns:
		[] if not found any trip to the desired city,
		bject: have information like price, duration, city of destiny, types of seats. The object have the attributes: 

		"id"              <--- ID

    	"name"           <--- Name of company

    	"price_confort"  <--- value of trip in confort mode

    	"price_econ"     <--- value of trip in economic mode

    	"city"           <--- City of destiny

    	"duration"       <--- Duration of trip

    	"seat"           <--- seat (economic mode)

    	"bed"            <--- sleeper seats (confort mode)
	"""
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
	"""
	Search for the fastest option for a city

	Args:
		city (string): Codade que deseja buscar

	Returns:
		[] if not found any trip to the desired city,
		bject: have information like price, duration, city of destiny, types of seats. The object have the attributes: 

		"id"              <--- ID

    	"name"           <--- Name of company

    	"price_confort"  <--- value of trip in confort mode

    	"price_econ"     <--- value of trip in economic mode

    	"city"           <--- City of destiny

    	"duration"       <--- Duration of trip

    	"seat"           <--- seat (economic mode)

    	"bed"            <--- sleeper seats (confort mode)
	"""
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

	if fastest != [] and cheapest != []:

		if fastest == cheapest:
			result.append(fastest)
		elif int(fastest['duration'].replace('h', '')) == int(cheapest['duration'].replace('h', '')):
			result.append(cheapest)
		else:
			result.append(fastest)
			result.append(cheapest)
	else:
		if fastest != []:
			result.append(fastest)
		elif cheapest != []:
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


