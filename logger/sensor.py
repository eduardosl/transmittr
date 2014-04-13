#import Adafruit_BBIO.ADC as ADC # for production
import ADC_synthetic as ADC # For testing
import sys
ADC.setup()

class Sensor:
  def __init__(self, *args, **kwargs):
    if len(args) == 1:
      attributes = args[0]
    elif len(args) == 6:
      attributes = {'description': args[0],
                'units': args[1],
                'scale_factor': args[2],
                'port': args[3],
                'nominal_level': args[4],
                'allowed_excursion': args[5],
                'last_raw_value': 0
    }
    else:
      raise AttributeError('Wrong number of attributes passed to constructor')

    self.description = attributes['description']
    self.units = attributes['units']
    self.scale_factor = float(attributes['scale_factor'])
    self.port = attributes['port']
    self.nominal_level = float(attributes['nominal_level'])
    self.allowed_excursion = attributes['allowed_excursion'] # in percent
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

  def __str__(self):
    print self.description + ' sensor'