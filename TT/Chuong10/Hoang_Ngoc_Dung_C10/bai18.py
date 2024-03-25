Smax = -1
Smin = 10e10

while True:
    score_input = input("Enter football score in the format winning score-losing score (e.g., 27-13) or type 'done' to finish: ")
    if score_input == 'done':
        break
    
    score_list = score_input.split('-')
    
    winning_score = int(score_list[0])
    losing_score = int(score_list[1])

    Smax = max(Smax,max(winning_score,losing_score))
    Smin = min(Smin,min(winning_score,losing_score))

print(f"Highest score: {Smax}")
print(f"Lowest score: {Smin}")