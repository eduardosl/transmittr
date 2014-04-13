from logger.logger import Logger
from logger.sensor import Sensor
from logger.DB import DB
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

if __name__== "__main__": 
	db = DB()
	l = Logger(db)
	l.load_sensors_from_db()
	#l.add_sensor_list(sensors)
	while True:
	  l.check_and_log_reading()
	  time.sleep(1)

