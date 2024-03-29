import random
from os import system
import time

def crate_ma(lst):
    number = random.sample(range(1,14),13)
    l = number * 2
    random.shuffle(l)

    for i in range(0,25,5):
        lst.append(l[i:i+5])
        
def printlist(lst):
    for i in lst:
        for j in i:
            if (j == 'Done'):
                print('Done', end = ' ')
            else :print('-', end = ' ')
        print('\n')
    
def gameplay(lst):
    i = 1
    print("Tunrn ", i)
    x = int(input('Enter the X coordinate(0 -> 4): '))
    y = int(input('Enter the Y coordinate(0 -> 4): '))
    currX = x
    currY = y
    i += 1
    while lst != []:
        print("Turn ", i)
        x = int(input('Enter the X coordinate (0 -> 4): '))
        y = int(input('Enter the Y coordinate (0 -> 4): '))
        print('The number is: ', lst[x][y])
        print('The number current is: ', lst[currX][currY])
        if lst[x][y] == lst[currX][currY]:
            lst[x][y] = 'Done'
            lst[currX][currY] = 'Done'
        currX = x
        currY = y
        i += 1
        printlist(lst)


if __name__ == '__main__':
    lst=[]
    crate_ma(lst)
    print("Memory game!!")
    print("This is a matrix of numbers")
    for i in lst:
        print(i)
    time.sleep(2)
    system('cls')
    gameplay(lst)
    