import DB

db = DB.DB()

db.c.flushdb()

def test_add_string_entry():
	key = 'Characters'
	value = 'Winnie the Pooh'
	db.add_entry(key, value)
	assert db.get_entry(key) == value

def test_add_dated_entry():
	import datetime
	date = datetime.datetime.now()
	page = 'Meteorite impacts'
	value = 'Siberia'
	db.add_dated_entry(page, date, value)
	assert db.get_latest_entry(page) == value

def test_get_latest_entry_from_empty_page():
    assert db.get_latest_entry('') is None

def test_get_last_n_entries():
	import time, datetime
	n = 2
	N = 10
	assert n <= N
	page = "Small numbers"
	import datetime, time, random
	x = [str(random.random()) for i in xrange(N)]
	for e in x:
		# print 'Adding ', e
		time.sleep(0.5) 
		db.add_dated_entry(page, datetime.datetime.now(), e)
	last_n_entries = db.get_last_n_entries(page, n)
	for l, e in zip(last_n_entries, x[N-n:]):
		print l, e
	assert sum([1*(l==e) for l,e in zip(last_n_entries, x[N-n:])]) == n


test_add_string_entry()
test_add_dated_entry()
test_get_latest_entry_from_empty_page()
test_get_last_n_entries()

