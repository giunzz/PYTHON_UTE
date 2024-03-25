def large_straight():
    p = 1 
    t = 1
    for i in range(1,6):
        p *= i
        t *= 6
    return 2*p/t

def coin(n,k):
    t = 2 ** n
    s = 1
    for i in range(1, k+1):
        s = s * (n - k + i) / i
    print (s)
    print(t)
    return s/t  
# ( Ckn / 2 ^ n)

if __name__ == '__main__':
    p = 1/6
    q = 1 - p
    print("The probability single Rolling all 5 dice",  p **5)
    print("A large straight is a roll where the dice come out 1-2-3-4-5 or 2-3-4-5-6 in any order:", large_straight())
    print("average longest run of heads or tails when flipping a coin 200 times", (0.5) ** (200-1))
    print("Estimate the average number of coin flips it takes before the string s comes up")
    n = int(input("Number of flips (n): "))
    k = int(input("Desired number of heads (k):"))
    print(coin(n,k))