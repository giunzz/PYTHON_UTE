from math import factorial

def Pascal(n):
  for i in range(n):
    for j in range(n-i+1):
      print(end=" ")
    for j in range(i+1):
      print(factorial(i)//(factorial(j)*factorial(i-j)), end="   ")
    print()
    
if __name__ == '__main__':
    n = int(input('Nhap so hang: '))
    Pascal(n)