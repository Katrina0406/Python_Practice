
import calendar

# create a plain text calendar with column starts at Sunday
c = calendar.TextCalendar(calendar.SUNDAY)
# (year, month, vertical spacing, horizontal spacing)
st = c.formatmonth(2017, 8, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017,1)
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# find the first friday of every month(meeting day)
print("Team meetings will be on:")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))
