
birthday_input = input("Enter a date in the format MM/dd/yy: ")

month = birthday_input[0:2]
day = birthday_input[3:5]
year = birthday_input[6:8]

months_list = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

if int(year) <= 24:
    print(f"{months_list[int(month)]} {day}, {2000+ int(year)}")
else:
    print(f"{months_list[int(month)]} {day}, {1900+ int(year)}")

