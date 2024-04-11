def number_of_factors(n):

    for i in range(1,n+1):
        if n % i == 0:
            print(i)
            
    


print(number_of_factors(20))