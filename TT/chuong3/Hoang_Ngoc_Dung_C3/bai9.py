print("EX 9:")
hour = int(input("Enter the hour between 1 and 12: "))
x = int(input(("How many hours ahead? ")))
print("New hour: ", (hour + x ) % 12 ,"o'clock")
