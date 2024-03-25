#find all integer solutions to the equation x^2 - 2y^2 = 1. We can do this by brute force, by trying all possible values of x and y in some range. Write a program that finds all integer solutions to this equation for x and y between 1 and 100. (Hint: you can use two nested loops to try all possible pairs of x and y in this range.)
if __name__=='__main__':
    print ("Finds all interger solution to x^2 - 2y^2 = 1")
    for i in range(1,101):
        for j in range(1,101):
            if i**2-2*j**2==1:
                print(i,j)
