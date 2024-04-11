def is_sorted(input_list):
    flag = 0
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            flag = 1
            break
    if flag == 0:
        print("The list is sorted")
    else:
        print("The list is not sorted")


is_sorted([1, 2, 7, 4])

