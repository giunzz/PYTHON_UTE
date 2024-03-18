def common(a,b):
    count = [a[i] for i in range(5) if a[i] == b[i]]
    return len(count)

def check(a,b):
    c = ''
    for i in range(5):
        if a[i] == b[i]: 
            c += a[i]
    return len(c)

l = ['01265','12171', '23257', '34548', '45970', '56236', '67324', '78084', '89872', '99414']
if __name__ == '__main__':
    
    for i in range (100000,99999):
        for x in l:
            if check(str(i), x) != 1:
                break
        else:
            print('The number is: ', i)