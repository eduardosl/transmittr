from logger import Logger
from sensor import Sensor
from DB import DB
import time
import Queue
import threading

# called by each thread
# def get_url(q, url):
#     q.put(urllib2.urlopen(url).read())

# theurls = '''http://google.com http://yahoo.com'''.split()

# q = Queue.Queue()

# for u in theurls:
#     t = threading.Thread(target=get_url, args = (q,u))
#     t.daemon = True
#     t.start()

# s = q.get()
# print s


sensors = [Sensor('Forward power', '\%', 1, 'P9_37', .8, .5),
           Sensor('Reflected power', '\%', 1, 'P9_38', .5, 1),
           Sensor('Temperature', 'Fahrenheit', 1, 'P9_39', .5, .8)]

print __name__
if __name__== "__main__": 
	db = DB()
	l = Logger(db)
	l.add_sensor_list(sensors)
	while True:
	  l.check_and_log_reading()
	  time.sleep(1)

