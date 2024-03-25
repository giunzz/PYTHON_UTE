count_Fer = 0
count_25th = 0

while True:
    birthday_input = input("Enter a birthday in the format month/day or type 'done' to finish: ")
        
    if birthday_input.lower() == "done":
        break
        
    birthday_list = birthday_input.split('/')
        
    month = int(birthday_list[0])

    day = int(birthday_list[1])
    if month == 2:
        count_Fer += 1
    if day == 25:
        count_25th += 1

print(f"There are {count_Fer} birthday in Ferbruary")
print(f"There are {count_25th} birthday in 25th")
