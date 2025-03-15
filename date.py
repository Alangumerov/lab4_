#1
  import datetime 
  current_date=datetime.date.today()

  five=current_date - datetime.timedelta(days=5) formatted_date=five.strftime('%d-%m-%Y')

  print(formatted_date)


#2
 import datetime

 current_date = datetime.date.today()
 yesterday_data = current_date - datetime.timedelta(days=1)
 tommorow_data = current_date + datetime.timedelta(days=1)

 formatted_current_date = current_date.strftime('%d-%m-%Y')
 formatted_yesterday_data = yesterday_data.strftime('%d-%m-%Y')
 formatted_tommorow_data = tommorow_data.strftime('%d-%m-%Y')

 print(formatted_current_date)
 print(formatted_yesterday_data)
 print(formatted_tommorow_data)

#3
import datetime

current_date = datetime.datetime.now()
current_date2 = current_date.replace(microsecond=0)

print(current_date)
print(current_date2)



#4
import datetime

date1 = datetime.datetime(2025, 2, 21, 14, 30, 0)
date2 = datetime.datetime(2025, 2, 22, 16, 45, 0)
time_difference = date2 - date1
seconds_difference = time_difference.total_seconds()

print(seconds_difference)
