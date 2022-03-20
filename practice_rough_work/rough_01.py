import json
import jsonpath

# Reading json
# https://airportcodes.io/en/country/india/

json_file = open("..\\input\\airportlocation.json")
flight_locations = json.loads(json_file.read())

location_from = flight_locations[0]
location_to = flight_locations[1]

frm = location_from['IATA']
print(frm)

to = location_to['IATA']
print(to)
