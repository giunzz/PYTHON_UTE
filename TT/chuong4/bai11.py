user = int(input("Enter hour: "))
day = int(input('enter am (1) or pm (2) : '))
hour = eval(input('How many hours ahead ?: '))

new = (user + hour) % 24
if (day % 2 + 1 == 2 ): print("New hour: ", new - 12 , "pm")
else: ("New hour: ", new , "am")
