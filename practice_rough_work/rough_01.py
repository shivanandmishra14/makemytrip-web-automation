import json
import json
import jsonpath

# Reading json
# https://airportcodes.io/en/country/india/

json_file = open("C:\\Users\\shiva\\Downloads\\SDET-DevOps\\makemytrip-web-automation\\input\\airportlocation.json")
flight_locations = json.loads(json_file.read())

location_from = flight_locations[4]
location_to = flight_locations[5]

to = location_to['IATA']
print(to)
frm = location_from['IATA']
print(frm)
