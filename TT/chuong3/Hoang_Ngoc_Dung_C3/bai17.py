print("EX 17:")
import calendar
Y = int(input("Enter a year: "))
print("A year is a leap year: ", calendar.isleap(Y))

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)