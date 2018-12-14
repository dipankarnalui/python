from datetime import datetime, timedelta
'''
today = datetime.today()
yesterday = today - timedelta(1)
only_date_str=str(yesterday).split()[0]
print(only_date_str)
'''

now = datetime.now()
today=now.strftime('%m-%d-%y')
print(today)

yesterday_with_time = now - timedelta(days=1)
yesterday=yesterday_with_time.strftime('%m-%d-%y')
print(yesterday)

day_before_yesterday_with_time = now - timedelta(days=2)
day_before_yesterday=day_before_yesterday_with_time.strftime('%m-%d-%y')
print(day_before_yesterday)





