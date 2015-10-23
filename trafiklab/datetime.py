from datetime import datetime

dt = datetime.strptime('2015-12-2T12:05:10', '%Y-%m-%dT%H:%M:%S')

dt2 = datetime.now()

timediff=dt2-dt

print timediff

print "{hour}:{minute:02d}".format(hour=dt.hour, minute=dt.minute)