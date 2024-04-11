# . Write a function called number_of_factors that takes an integer and returns how many
# factors the number has

def number_of_factors(n):
    count=0
    for i in range(1,n+1):
        if n % i == 0:

            count+=1
    print(count)


print(number_of_factors(20))