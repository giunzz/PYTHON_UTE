from random import randint
outcome ={2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0,10: 0,11: 0,12: 0} # khong gian mau
sim =1000

for i in range(sim):
    first_dice_roll = randint(1,6)
    second_dice_roll = randint(1,6)
    dice_roll = first_dice_roll + second_dice_roll
    outcome[dice_roll] +=1
for i in outcome.keys():
    print(i , ":" ,outcome[i]/sim * 100 , "%")