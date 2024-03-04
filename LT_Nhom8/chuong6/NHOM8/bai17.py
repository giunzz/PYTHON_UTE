def Q_a(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

def Q_b(s1, k):
    count = 0
    for i in range(len(s1)):
        if i == k:
            count += 1
    return count

def Q_c(s1, s2):
    if s1 <= s2:
        return True
    else:
        return False

def Q_d(s1):
    return s1.upper()

def Q_e(s1):
    return len(s1)

def Q_f(s1):
    return s1.lower()

def main():
    city1 = "London"
    city2 = "Paris"
    city3 = "London"
    city4 = "Sydney"
    print(Q_a(city1, city2))
    print(Q_b(city3, 'n'))
    print(Q_c(city1, city4))
    print(Q_d(city2))
    print(Q_e(city4))
    print(Q_f(city1))

if __name__ == "__main__":
    main()