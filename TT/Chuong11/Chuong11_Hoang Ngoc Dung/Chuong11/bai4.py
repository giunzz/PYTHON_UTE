d = {'Dung':'dung123','Dat':'dat123','hung':'hung123','hungg':'hungg123','my':'my123','virt':'virt123',
'numerical':'numerical123','nga':'num123' ,'bich':'bich123','mai':'mai123'}
n = input(' enter their username:')
if n not in  d.keys() :
    print('the person is not a valid user of the system')
else :
    print('the person is a valid user of the system')
    p = input('enter their password: ')
    if p != d[n] :
        print('the person is not a valid user of the system')
    else :
        print('you are now logged in to the system')