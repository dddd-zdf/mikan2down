import datetime
now = datetime.datetime.now().strftime("%Y-%m")
time = datetime.datetime.now().timetuple()
today = now +"-"+ str(time.tm_mday)
print(today)