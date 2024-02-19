# print("EX1 and EX2: ")
# s1 = 0
# s4 = 0 
# s9 = 0
# for i in range(2,100):
#     if (i * i > 100): break
#     else: 
#         if ((i*i) % 10 == 1): s1 = s1 + 1
#         if ((i*i) % 10 == 4): s4 = s4 + 1
#         if ((i*i) % 10 == 9): s9 +=  1
        
# print("The squares of the numbers from 1 to 100 end in 1: ", s1)
# print("The squares of the numbers from 1 to 100 end in 4: ", s4)
# print("The squares of the numbers from 1 to 100 end in 9: ", s9)

# from numpy import log as ln
# print("EX3: ")
# n = int (input("Enter a number: "))
# s = 1
# for i in range(2,n + 1):
#     s += 1/i
# print("Answer: %.4f" %(s - ln(n)))

# print("EX4: ")
# s = 0
# for i in range(1,2001):
#     if (i % 2): s += i
#     else : s -= i
# print("Answer: ", s)

# print("Ex5:")
# n = int(input("Enter a number: "))
# s = 0
# for i in range(1,n + 1):
#     if (n % i == 0): s += i
# print("The sum of the divisors of a number: ", s)

print("Ex8: ")
s1 = int(input("Enter the first side: "))
s2 = int(input("Enter the second side: "))
s1,s2 = s2,s1
print("Swap: ", s1 , "," , s2)

