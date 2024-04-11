def one_away(s1, s2):
    if len(s1) != len(s2):
        print(f"The strings are not one away.")
        return 0
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
            if diff > 1:
                print(f"The strings are not one away.")
                return 0
    print(f"The strings are one away.")
    
one_away('wafer','water')

    