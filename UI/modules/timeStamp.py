import time
import datetime

def formatTime(s):
    return str(int(time.mktime(datetime.datetime.strptime(s, "%d-%m-%Y"))))

def getTimestamp(s):
    #2018-03-03+12:50
    return str(int(time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M").timetuple())))
    # return str(int(time.mktime(datetime.datetime.strptime(s, "%d-%m-%Y - %H:%M").timetuple())))

def getTimeFromTimestamp(s):
    return datetime.datetime.fromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')
