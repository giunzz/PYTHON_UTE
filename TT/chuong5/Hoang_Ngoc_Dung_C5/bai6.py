print("Ex6 ")
n = 100
prime = [False for i in range(n + 1)]

def sumab(a,b):
    return a + b

def ss(n):
    prime[0] = prime[1] = True
    for i in range (2,n + 1):
        if (not prime[i]):
            for j in range(i * i, n + 1, i):
                prime[j] = True
if __name__=='__main__':
    ss(n)
    print("The perfect numbers that are less than 10000: ", end = "")
    for i in range(2,n + 1):
        if (not prime[i]):
            p =  pow(2 , (i - 1)) * (pow(2,i) - 1)
            if (p > 10000): break
            print(p, end =" ")
    
    


    
    

