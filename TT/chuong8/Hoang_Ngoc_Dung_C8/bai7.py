from random import sample
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test = 0
total_test = 1000

for i in range(total_test):
    user = sample(num, 6)
    user = sorted(user)
    draw = 0
    while True:
        draw += 1
        if user == sorted(sample(num, 6)):
            break
    test += draw

avg = test / total_test
print(f"Average number of drawings needed: {avg}")
