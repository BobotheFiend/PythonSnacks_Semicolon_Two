#collect the year
#if the year is divisible by 4 without a remainder its a leap year
#or use datetime class
from datetime import datetime

user_input = int(input("Enter the year: "))

#is_leap_year = datetime(user_input,2,29)
#
#try:
#    if is_leap_year == is_leap_year:
#        print(" a Leap Year!")
#except ValueError:
#    if is_leap_year != is_leap_year:
#        print("Not a leap year")

if user_input % 4 == 0:
    print("A Leap Year")
else:
    print("Not a Leap Year")
