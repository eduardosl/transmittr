import DB
import sys
import datetime
import notify
from sensor import Sensor
import json

class Logger:
  def __init__(self, db):
    self.db = db
    self.sensors = []
    self.crap = []

  def add_sensor(self, sensor):
    self.sensors.append(sensor)

  def add_sensor_list(self, sensors):
    self.sensors += sensors

  def load_sensors_from_db(self):
    sensor_hash = self.db.get_hash('sensors')
    for sensor_attributes in sensor_hash.values():
      # Terribly unsafe idea for getting around redis returning a hash whose values
      # have been serialized into strings (and were originally dicts)
      sensor_attributes = eval(sensor_attributes)
      self.add_sensor(Sensor(sensor_attributes))

  def list_sensors(self):
    return sorted(self.sensors, key=lambda x: x.get_description())

  def take_reading(self):
    # A reading consists of a tuple (value, isNormal) indicating the scaled reading
    # and whether the reading is within the allowed excursion range, respectively
    now = datetime.datetime.now()
    reading = {}
    for sensor in self.sensors:
      reading[sensor.get_description()] = (sensor.get_value(), sensor.value_within_range())
    return now, reading

  def check_reading(self):
    abnormal_sensors = []
    now, reading = self.take_reading()
    for sensor in self.sensors:
      if not sensor.value_within_range():
        abnormal_sensors.append(sensor)
    if len(abnormal_sensors) > 0:
      notify.notify_abnormal_reading(now, abnormal_sensors)
    return now, reading

  def check_and_log_reading(self):
    now, reading = self.check_reading()
    self.log(now, reading)

  def log(self, time, reading):
    for key in reading:
      self.db.set_dated_entry(key, time, reading[key])
  
  def print_log():
    pass