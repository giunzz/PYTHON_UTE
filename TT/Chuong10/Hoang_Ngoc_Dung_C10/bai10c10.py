# Adding certain numbers to their reversals sometimes produces a palindromic number. For
# instance, 241 + 142 = 383. Sometimes, we have to repeat the process. For instance, 84 + 48 =
# 132 and 132 + 231 = 363. Write a program that finds both two-digit numbers for which this
# process must be repeated more than 20 times to obtain a palindromic number.
for num in range(10, 100):
    iterations = 1
    result = num + int(str(num)[::-1])
    while 1:
        if iterations == 20: 
            if str(result) == str(result)[::-1] : print(num)
            break
        result += int(str(result)[::-1])
        iterations += 1

        
        

