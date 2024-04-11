days_in_months = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31
}

m = input("Enter name of month: ")

if m not in days_in_months:
    print("Please enter the correct month")
else:
    print("There are", days_in_months[m], "days in", m)

print("Months in alphabetical order are:", sorted(days_in_months))

print("Months with 31 days:", end=" ")
for i in days_in_months:
    if days_in_months[i] == 31:
        print(i, end=" ")

day_month_lst = []
for i in days_in_months:
    day_month_lst.append([days_in_months[i], i])
day_month_lst.sort()

month_day_lst =[]
for i in day_month_lst:
    month_day_lst.append([i[1], i[0]])

sorted_days_in_months = dict(month_day_lst)
print()
print("Months sorted by days:", sorted_days_in_months)
