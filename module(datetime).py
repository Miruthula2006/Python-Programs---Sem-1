"""
import datetime
#current date and time
c_datetime=datetime.datetime.now()
#current date only
print(c_datetime)
c_date=datetime.date.today()
print(c_date)
#current time only
c_time=datetime.datetime.now().time()
print(c_time)
#create specific date(year,month,date)
s_date=datetime.date(2024,10,9)
print(s_date)
#create specific time(hour,minute,second)
s_time=datetime.time(9,5,10)
print(s_time)
#create specific date and time(year,month,day,hour,minute,second)
s_datetime=datetime.datetime(2024,10,9,9,5,10)
print(s_datetime)
#formating date and time into a string
f_date=c_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f_date)
#parsing a date string into a datetime object
date_string="2024-10-09 09:05:10"
parsed_date=datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print(parsed_date)
#create a timedelta of 10 days
ten_days=datetime.timedelta(days=10)
#subtract 10 days from the current date
ten_days_ago=c_date-ten_days
print(ten_days_ago)
#add 10 days to the current date
ten_days_later=c_date+ten_days
print(ten_days_later)
#calculate difference between 2 dates
date1=datetime.date(2024,10,19)
date2=datetime.date(2023,10,9)
d=date1-date2
print(d)"""
import calendar
year = 2024
month = 10
print(calendar.month(year, month))
# Print the calendar for the given year
print(calendar.calendar(year))
# Check if the year is a leap year
is_leap = calendar.isleap(year)
print(f"{year} is a leap year: {is_leap}")
# Get the first weekday and the number of days in the month
first_weekday, num_days = calendar.monthrange(year, month)
print(f"First weekday: {first_weekday}, Number of days: {num_days}")
for day in calendar.Calendar().itermonthdays(year, month):
    if day!=0:
       print(day)
import calendar
# Create a TextCalendar instance
text_cal = calendar.TextCalendar(calendar.SUNDAY) # SUNDAY as the starting day of the week
# Generate a plain-text calendar for a specific month
year = 2024
month = 10
plain_text_cal = text_cal.formatmonth(year, month)
# Print the plain-text calendar
print(plain_text_cal)
from datetime import datetime, timedelta
# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")
# Specify how many days/hours/minutes in the past you want to go
days_in_past = 5
hours_in_past = 3
minutes_in_past = 30
# Subtract time using timedelta
past_time = now - timedelta(days=days_in_past, hours=hours_in_past, minutes=minutes_in_past)
print(f"Past date and time (5 days, 3 hours, 30 minutes ago): {past_time}")
#Example : Change the first letter to caps..
# Example of capwords function
import string

sentence = "hello world from python"
capitalized_sentence = string.capwords(sentence)
print(capitalized_sentence)
