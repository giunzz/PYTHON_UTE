def first_diff(str1, str2):
  
  # Iterate through characters of both strings simultaneously
  for i in range(min(len(str1), len(str2))):
    if str1[i] != str2[i]:
      return i
  # If loops completes, strings are identical
  return -1

# Example usage:
string1 = "hello"
string2 = "helo"
index = first_diff(string1, string2)
print(index)  # Output: 1

string1 = "apple"
string2 = "apple"
index = first_diff(string1, string2)
print(index)  # Output: -1