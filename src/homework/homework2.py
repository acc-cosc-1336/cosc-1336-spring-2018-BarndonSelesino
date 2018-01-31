hour = float(input("please enter the number of hours:      '))
if hour > 24 or hour < 0:
  print('Invalid hours')
time_type12 = hour <= 12 and hour >= 1:

time_type24 = hour <= 23 and hour >= (1,12):

time_type = time_type12 or time_type24:

minute = float(input('Please enter the number of minutes:     '))
if minute > 59 or minute < 0:
  print ('invalid minutes')
second = float(input('Please enter the number of seconds:    '))
if second > 59 or second < 0:
  print('Invalid seconds')
if hour < 10
  hour = "0" + str(hour)
if minute < 10
  minute = "0" + str(minute)
if second < 10
  second = "0" + str(second)
get_time = (hour, minute, second, time_type, meridium)
meridium = hour
if meridium >= 12 and meridium <= 23:
  print('pm')
elif meridium <= 11 and meridium == 24:
  print('am')
  
 get_time(): 
