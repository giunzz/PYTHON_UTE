#check 1 number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 100
prime = [False for i in range(n + 1)]

def ss(n):
    prime[0] = prime[1] = True
    for i in range (2,n + 1):
        if (not prime[i]):
            for j in range(i * i, n + 1, i):
                prime[j] = True
if __name__=='__main__':
    ss(n)
    print("So nguyen to :")
    for i in range(1,100):
        if (not prime[i]):
            print(i, end =" ")
    

