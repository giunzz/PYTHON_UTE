list_1=[11,5,6,4,0]
list_2 =[1,7,9,68,2]
list_common_items =[]
for i in list_1:
    if i in list_2:
        have_common = True
        print('have_common')   
        break
    else:
        print('not have_common')
        break