L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
gaps = [L[i+1] - L[i] for i in range(len(L)-1)]

max_gap = max(gaps)

count_gaps_of_size_2 = gaps.count(2)
percentage_gaps_of_size_2 = (count_gaps_of_size_2 / len(gaps)) * 100

print("List of gaps between consecutive entries:", gaps)
print("Maximum gap size:", max_gap)
print("Percentage of gaps that have size 2:", percentage_gaps_of_size_2, "%")
