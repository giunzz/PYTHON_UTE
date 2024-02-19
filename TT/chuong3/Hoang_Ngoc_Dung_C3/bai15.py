print("EX 15:")
import math
for i in range(0,346,15):
    j = math.radians(i)
    print(i,"--- " , end =" " )
    print('%.4f'% math.sin(j), end =" ")
    print('%.4f' %math.cos(j))
