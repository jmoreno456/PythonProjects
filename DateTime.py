# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%A, %B %d, %Y - %I:%M %p"))


# from datetime import date, timedelta

# today = date.today() # get current date from date library
# deadline = today + timedelta(days=30)

# print("Today's date:", today)
# print("Deadline in 30 days:", deadline)


# from datetime import date, timedelta

# today = date(2025, 6, 1)
# next_date = today - timedelta(days=10)

# print(next_date)


# from datetime import datetime, date

# def birthday(date):
# date = input("When is your birthday(YYYY-MM-DD): ")
# return datetime.strftime(date, "%Y-%M-%d")

# my_bday = birthday(date)
# print("Your birthday is:", my_bday)


## practice
# from datetime import datetime, date


# def birthday_countdown():
# bday_str = input("When is your birthday? (YYYY-MM-DD): ")
# bday_date = datetime.strptime(bday_str, "%Y-%m-%d").date()

# today = date.today()
# this_year_bday = bday_date.replace(year=today.year)

# if this_year_bday < today:
# this_year_bday = this_year_bday.replace(year=today.year + 1)

# days_left = (this_year_bday - today).days
# print("Days until your next birthday:", days_left)


# birthday_countdown()


import time
from datetime import datetime


def get_future_date():
    while True:
        str_date = input("When is your graduation date? (YYYY-MM-DD): ")
        try:
            return datetime.strptime(str_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")


def format_countdown(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"


target_date = get_future_date()

print("Countdown started. Press Ctrl+C to exit.\n")
while True:
    now = datetime.now()
    delta = target_date - now

    if delta.total_seconds() <= 0:
        print("\nCountdown finished!")
        break

    print(f"\rTime remaining: {format_countdown(delta)}", end="", flush=True)
    time.sleep(1)
