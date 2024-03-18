m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
sum = 0
count = 0

for row in m:
   
    for num in row:
        
        sum += num
      
        count += 1


average = sum / count


print("Average of all entries in the 4x4 list:", average)
