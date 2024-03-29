# Write a program that allows the user to enter any number of test scores. The user indicates
# they are done by entering in a negative number. Print how many of the scores are A’s (90 or
# above). Also print out the average.

def main():
    scores = []
    while True:
        score = int(input("Enter a score: "))
        if score < 0:
            break
        scores.append(score)
    average = sum(scores) / len(scores)
    if average >= 90:
        print(f"Average: {average:.2f}")
    else:
        print(f"Average: {average:.2f}")
    print(f"Number of A’s: {sum(score>=90 for score in scores)}")
if __name__ == "__main__":  
    main()

