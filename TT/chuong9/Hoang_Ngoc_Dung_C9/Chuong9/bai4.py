print('Enter correct username and password combo to continue')
count=5
password =''
while password!='truongdaihocspkt' and count > 0 :
    password=input('Enter password: ')

    if password == 'truongdaihocspkt':
     print('Access granted')

    else:
        print('Access denied. Try again.')
        count-=1