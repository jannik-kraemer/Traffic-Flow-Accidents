import time
import datetime

def getTime(s):
    return str(int(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y - %H:%M").timetuple())))