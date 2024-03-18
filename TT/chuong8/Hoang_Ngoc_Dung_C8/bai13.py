#Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
#following.
#(a) A list that consists of the strings of s with their first characters removed
#(b) A list of the lengths of the strings of s
#(c) A list that consists of only those strings of s that are at least three characters long



L = ["tao", "chuoi", "oi", "bi", "nho"]
result_a = [s[1:] for s in L]
result_b = [len(s) for s in L]
result_c = [s for s in L if len(s) >= 3]

print("List with first characters removed:", result_a)
print("List of lengths of strings:", result_b)
print("List of strings with length at least three:", result_c)
