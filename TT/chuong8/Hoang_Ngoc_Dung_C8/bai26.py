def print_right(n,m):
    x = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            print('(', i - 1,',',j - 1, ')' , end = '  ')
            if (m == j): 
                for z in range(3): 
                    print(x, end = ' ')
                    x += 1
        print('\t')

def print_left(n,m):
    x = 0
    for i in range(1,n+1):
        for z in range(3): 
                    print(x, end = '  ')
                    x += 1
        for j in range(1,m+1):
            print('(', i - 1,',',j - 1, ')' , end = '')
        print('\t')
if __name__=='__main__':
    n = int(input('Enter a row number: '))
    m = int(input('Enter a column number: '))
    print_right(n,m)
    print('-'*50)
    print_left(n,m)

