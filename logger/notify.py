import smtplib
import redis
from email.mime.text import MIMEText
import DB

def notify_abnormal_reading(time, abnormal_sensors):
	#DB.get_value('Notification Settings')
  	msg = 'Abnormal readings on ' + \
  		   time.strftime('%b %d, %Y at %H:%M:%S') + ":\n"
  	for sensor in abnormal_sensors:
  		last_value = sensor.get_value(refresh=False)
    	if last_value < 0: 
      		msg += sensor.get_description() + ": failed to read"
    	else:
      		msg += sensor.get_description() + ": " + str(sensor.get_value(refresh=False))

	msg = MIMEText(msg)

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'WMBR Transmitter Abnormal Readings'
	msg['From'] = 'WMBR robot engineer <no-reply@wmbr.org>'
	msg['To'] = ''

	print msg.as_string() 

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP("smtp.gmail.com:587")
	s.starttls()
	#s.sendmail('no-reply@wmbr.org', [''], msg.as_string())
	s.quit()
