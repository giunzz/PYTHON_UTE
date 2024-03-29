from random import randint
point = 0
i = 1
point_comp = 0
while point < 3 and point_comp <3:
    comp = randint(1, 3)
    opt = eval(input(f"Hay chon Rock (1), Paper (2) hoac Scissors(3) - vong {i}: "))
    if opt == 1:
        if comp == 1:
            point += 0
        if comp == 2:
            point_comp += 1
        if comp == 3:
            point += 1
    if opt == 2:
        if comp == 1:
            point += 1
        if comp == 2:
            point += 0
        if comp == 3:
            point_comp += 1
    if opt == 3:
        if comp == 1:
            point_comp += 1
        if comp == 2:
            point += 1
        if comp == 3:
            point += 0
    print(f'Your point is: {point}')
    print(f'Computer point is: {point_comp}')
    print()
    if point == 3 or point_comp == 3:
        print('The game is finished')
    i += 1