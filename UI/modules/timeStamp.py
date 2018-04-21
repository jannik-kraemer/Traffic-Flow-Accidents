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

def getDayOfWeek(date):
    # print("Input: " + s)
    dateFormatted = date.split(' ')[0]
    # timeFormatted = date.split(' ')[1]
    y = dateFormatted.split('-')[0]
    m = dateFormatted.split('-')[1]
    d = dateFormatted.split('-')[2]

    date = datetime.date(
        int(y), 
        int(m), 
        int(d)).weekday()
    return date + 1