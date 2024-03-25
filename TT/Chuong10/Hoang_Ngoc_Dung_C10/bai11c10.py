# Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
# apart. One such pair is 199991 and 200002

def is_palindromic(n):
    return str(n) == str(n)[::-1]

def main():
    palindromes = []
    for num in range(100000, 1000000):
        if is_palindromic(num):
            palindromes.append(num)
    for i in range(len(palindromes) - 1):
        if palindromes[i+1] - palindromes[i] < 20:
            print(palindromes[i], palindromes[i+1])

if __name__ == "__main__":
    main()