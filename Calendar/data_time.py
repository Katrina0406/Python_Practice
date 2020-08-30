
from datetime import date, time, datetime, timedelta

def main():
    # get today's date
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=sunday)
    print("Today's weekday # is: ", today.weekday())
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    print("Which is a: ", days[today.weekday()])

    # get today's date from datetime class
    today = datetime.now()
    print("The current date and time is ", today)

    # get the current time, date respectively
    t = datetime.time(datetime.now())
    d = datetime.date(datetime.now())
    print(t, d)

    #---------------------------------------------#
    # Time and dates can be formatted using a set of predefined string
    now = datetime.now()

    # %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - Day of month
    print(now.strftime("The current year is: %y"))
    print(now.strftime("%a, %d, %b, %y"))

    # %c - locale's date & time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))

    #---------------------------------------------#
    # construct a timedelta
    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date
    now = datetime.now()
    print("today is: " + str(now))

    # print today's date one year from now
    print("one year from now it will be: " + str(now + timedelta(days=365)))

    # create a timedelta that used more than one argument
    print("In 2 days and 3 weeks, it will be " + 
            str(now + timedelta(days=2, weeks=3)))

    # calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)

    # How many days until April Fool's Day
    today = date.today()
    afd = date(today.year, 4, 1)

    # use date comparison to see if April Fool's has gone for this year
    # If it has, use the next year's date
    if afd < today:
        print("April Fool's day already went by %d days ago" % (today-afd).days)
        afd = afd.replace(year = today.year+1)
    
    # Now calculate the amount of time until April Fool's Day
    time_to_afd = afd-today
    print("It's just ", time_to_afd.days, "days until April Fool's Day")

if __name__ == '__main__':
    main()
