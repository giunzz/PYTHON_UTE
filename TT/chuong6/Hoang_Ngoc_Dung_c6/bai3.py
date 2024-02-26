#exercise 3
def checkparenthesesbalance(formula):
    count = 0
    for char in formula:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def main():
    n = input("Entering formulas: ")
    a = checkparenthesesbalance(n)
    if a:
        print("Same number of open-ing and closing parentheses.")
    else:
        print("Not same number of open-ing and closing parentheses")

if __name__ == "__main__":
    main()
