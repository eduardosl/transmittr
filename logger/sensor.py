#import Adafruit_BBIO.ADC as ADC # for production
import ADC_synthetic as ADC # For testing
import sys
ADC.setup()

class Sensor:
  def __init__(self, description, units, scale_factor, port, nominal_level, allowed_excursion):
    self.description = description
    self.units = units
    self.scale_factor = scale_factor
    self.port = port
    self.units = units
    self.nominal_level = nominal_level
    self.allowed_excursion = allowed_excursion # in percent
    self.last_raw_value = 0

  def get_raw_value(self, refresh=True):
    if refresh:
      try:
        self.last_raw_value = ADC.read(self.port)
      except:
        e = sys.exc_info()[1]
        print "Read error for " + self.get_description() + " sensor: " + str(e)
        self.last_raw_value = -1
    return self.last_raw_value

  def get_value(self, refresh=True):
     return self.get_raw_value(refresh)*self.scale_factor

  def get_string_value(self, refresh=True):
    return str(self.get_value(refresh)) + ' ' + self.units
    
  def get_description(self):
    return self.description

  def value_within_range(self, value=None):
    if value is None:
      value = self.get_value(refresh=False)
    return abs((value-self.nominal_level)/self.nominal_level) < self.allowed_excursion