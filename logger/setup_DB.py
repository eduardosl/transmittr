# Clears any pre-existing sensors in the DB and adds 
# initial values for some pre-defined sensors

from DB import DB
from sensor import Sensor
import json

db = DB()
keys = db.get_hash_keys('sensors')
for key in keys:
	db.delete_hash('sensors', key)
#print db.get_hash('sensors')

sensors = [Sensor('Forward power', '\%', 1, 'P9_37', .8, .5),
           Sensor('Reflected power', '\%', 1, 'P9_38', .5, 1),
           Sensor('Temperature', 'Fahrenheit', 1, 'P9_39', .5, .8)]

sensors_hash = {}
for s in sensors:
	data = s.__dict__
	sensors_hash['sensor:' + s.description.replace(' ','',1000)] = data

db.set_hash('sensors', sensors_hash)

#print db.get_hash('sensors')