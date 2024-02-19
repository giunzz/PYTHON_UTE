from numpy import log as ln
n = int (input("Enter a number: "))
s = 1
for i in range(2,n + 1):
    s += 1/i
print("Answer: %.4f" %(s - ln(n)))
