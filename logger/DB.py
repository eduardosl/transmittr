import redis
import time

# This database is _not_ relational

# We'll use a key-value store, where keys are sensors and values are sensor readings.
# Furthermore, we'll use a sorted set store, where the date is used for sorting. 

class DB:
  def __init__(self):
    self.c = redis.StrictRedis(host='localhost', port=6379, db=0)

  def set_dated_entry(self, page, date, value):
  	unix_time = time.mktime(date.timetuple())
  	self.c.zadd(page, unix_time, value)

  def get_dated_entries(self, page, startdate, enddate):
  	unix_starttime = time.mktime(startdate.timetuple())
  	unix_endtime = time.mktime(startdate.timetuple())
  	return self.c.zrangebyscore(page, startdate, enddate)

  def get_latest_entry(self, page):
    latest = self.c.zrange(page, -1, -1)
    if len(latest) == 0:
      return None
    return latest[0]

  def get_last_n_entries(self, page, n):
    num_entries = self.c.zcard(page)
    return self.c.zrange(page, num_entries-n, -1, withscores=False)
  
  def set_entry(self, key, value):
    # WARNING: Casts floats and ints into strings!
  	self.c.set(key, value)

  def get_entry(self, key):
    return self.c.get(key)

  def set_hash(self, name, mapping):
    self.c.hmset(name, mapping)

  def get_hash(self, name):
    return self.c.hgetall(name)

  def get_hash_keys(self, name):
    return self.c.hkeys(name)

  def delete_hash(self, name, key):
    self.c.hdel(name, key)



