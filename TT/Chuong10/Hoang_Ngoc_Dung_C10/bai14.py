def find_smallest_integer():
  for num in range(1, 10**9): 
    str_num = str(num)
    moved_num = int(str_num[1:] + str_num[0]) 
    if moved_num == 3.5 * num:
      return num
  return None 
smallest_integer = find_smallest_integer()
if smallest_integer:
  print(f"The smallest positive integer satisfying the property is: {smallest_integer}")
else:
  print("No solution found within the search range.")