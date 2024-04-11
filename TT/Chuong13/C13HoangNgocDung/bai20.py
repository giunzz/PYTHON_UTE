def merge1(a,b):
    c = a + b
    print(type(c))
    c.sort()
    print('The list using sort method:')
    print(c)

def merge2(a,b):
    c = a + b
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i]>c[j]:
                c[i],c[j] = c[j],c[i]
    print('The list using bubble sort:')
    print(c)

if __name__ == '__main__':
    a = [int(i) for i in input ("enter the list:").split()]
    b = [int(i) for i in input('enter the list: ').split()]
    merge1(a,b)
    merge2(a,b)
    
    