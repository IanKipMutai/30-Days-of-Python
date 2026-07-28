from datetime import datetime , date

current = datetime.now()
day = current.day
month = current.month
year = current.year
hour = current.hour
minute = current.minute
timestamp = current.timestamp()
print(day)
print(month)
print(year)
print(hour)
print(minute)
print(timestamp)

formated_current = current.strftime('%m/%d/%Y, %H:%M:%S')
print(formated_current)

date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)

now = date.today()
future = date(year = 2027 , month= 1, day=1)
difference = future - now
print('difference :',difference)
