flag = 0
while flag == 0:
    len = float(input("Enter a length in centimeters: "))
    if (len >= 0): 
        flag = 1
        print("Convert length to inches:" '%.4f' % (len * 0.39370))
