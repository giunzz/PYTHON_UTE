print('Question a ')
n = int(input("Input number: "))
sum = 0
for i in range(1,n + 1):
    sum = sum + 1/i
print('Sum a : %.2f' % sum)

print('Question b ')
n = int(input("Input number: "))
sum = 0
for i in range(1,n + 1):
    sum = sum + pow(i,i-1)
print('Sum b : %.2f' % sum)
