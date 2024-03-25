from random import randint
print("Simulates all posssible rolls of four dice")

if __name__=='__main__':
    roll = [randint(1, 7) for i in range(10)]
    dd = [0 for i  in range(15)]
    for i in range(len(roll) - 1):
        dd[roll[i]] += 1
        for j in range(i + 1, len(roll)):
            tmp = roll[i] + roll[j]
            dd[tmp] += (tmp <= 12)
            print(roll[i], roll[j]) 
    print("Totals and percentages: ")
    
    for i in range(1,13): print(i, dd[i] / sum(dd) * 100 , "%")
            