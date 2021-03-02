#What is n days from now?
def what_day(today,how_many_days):
  list_of_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  today = "".join([char.lower() for char in today])
  for day in range(len(list_of_days)):
    now = "".join([char.lower() for char in list_of_days[day]])
    if now == today:
      today_index = day
      break
  return list_of_days[(today_index +(how_many_days % 7))%7]

#build string answer
def build_string(data,day=''):
  # no 00 (00 to 12)
  if data[0] == 0:
    text = '12'
  else:
    text = str(data[0])
  
  #if not include the name of day
  if not day:
    if data[1] < 10:
      text += ":0"
    else:
      text += ":"
    text += str(data[1]) + " " + data[2]
    if data[3] != '':
      text += " " + data[3]
  #if include the name of day
  else:
    tomorrow = what_day(day,data[4])
    if data[1] < 10:
      text += ":0"
    else:
      text += ":"
    text += str(data[1]) + " " + data[2] + ", " + tomorrow
    if data[3] != '':
      text += " " + data[3]
  
  return text

#create a string adverb of time
def future_day(day):
  if day == 1:
    msg = "(next day)"
  elif day == 0:
    msg = ""
  else:
    msg = "("+str(day)+" days later)"
  return msg

#calculation process
def addition_time(hour,hour_duration,minute,minute_duration,meridiem):
    if meridiem == "PM":
        hour += 12
    new_hour = hour + hour_duration
    new_minute = minute + minute_duration
    new_day = 0
    hour_temp = int(new_minute // 60)

    if new_minute >= 60:
        new_minute -= 60
    if hour_temp >= 1:
        for hr in range(hour_temp):
            new_hour += 1
    
    if new_hour // 24 > 0:
        for dy in range(int(new_hour // 24)):
            new_day += 1
            new_hour -= 24

    if new_hour >= 12:   
        meridiem = "PM"
        new_hour -= 12
    else:
        meridiem = "AM"   

    return [new_hour,new_minute,meridiem,future_day(new_day),new_day]
 
def add_time(start, duration, day=''):
  #get the time and convert string to integer 
  n_start = len(start)
  n_duration = len(duration)
  hour = int(start[0:n_start-6])
  minute = int(start[n_start-5:n_start-3])
  meridiem = start[-2:]
  hour_duration = int(duration[0:n_duration-3])
  minute_duration = int(duration[-2:])
  
  #call the addition process
  result = addition_time(hour,hour_duration,minute,minute_duration,meridiem)
  
  #call function to build the answer (string)
  if not day: 
    new_time = build_string(result)
  else:
    new_time = build_string(result,day)
  
  return new_time