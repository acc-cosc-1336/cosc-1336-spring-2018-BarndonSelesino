def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    '''
    Returns a time in 12 or 24 hour format

    :param hour: The hour of day-
                 when time_type 12 hr hour valid range 1 to 12 otherwise return 'Invalid hours(1-12)'
                 when time_type 24 hr hour valid range 0 to 23 otherwise return 'Invalid hours(range 0-23)'

    :param minutes: Minutes of an hour--minutes valid range 0 to 59 otherwise return 'Invalid minutes(range 0-59)'
    :param seconds:  seconds of an hour--seconds valid range 0 to 59 otherwise 'Invalid seconds(range 0-59)'
    :param time_type: Indicates the format of time to derive 12hr or 24hr
                      Valid time_type values 12 or 24 otherwise return 'Invalid time_type(12 or 24 only)'
                      If time_type is 24 ignore meridiem value;

                      If time_type is 12hr time use meridiem parameter value(AM or PM)

    :param meridiem:  AM, PM

    :return: time in 12 or 24 hour format
      Example for 12 hour format 09:09:09 PM
      Example for 24 hour format 21:09:09
    ADD YOUR CODE AFTER THE THREE QUOTES BELOW (dont forget to include a return statement at the end
    '''

        if minutes > 59 or minutes < 0:
          return 'Invalid minutes(range 0-59)'
        
        if seconds > 59 or seconds < 0:
          return 'Invalid seconds(range 0-59)'
        time = ''
        #write decision structure code here

        if time_type == 24:

        elif time_type == 12:

        else:
            return 'Invalid time_type(12 or 24 only)'
        if hour > 24 or hour < 0:
          print('Invalid hours')
        time_type12 = hour <= 12 and hour >= 1:

        time_type24 = hour <= 23 and hour >= (1,12):

    


        if hour < 10
          hour = "0" + str(hour)
        if minute < 10
          minute = "0" + str(minute)
        if second < 10
          second = "0" + str(second)

        time = (hour + ':'+ minute + second)
        
    
  
 get_time(): 
 

    return  time

def time_from_utc(utc_offset, utc_zero_time):
    '''
    Write code to calculate a time zone's time after applying utc_offset
    :param utc_offset:
    :param utc_zero_time:
    :return:
    DON NOT CHANGE ANYTHING IN THIS FUNCTION
    '''

    return (utc_zero_time + utc_offset) % 24
