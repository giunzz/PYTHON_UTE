import math
def check_perfect_squares(n):
    t = math.sqrt(n)
    if ( t * t == n): return True
    else : return False
def check_perfect_cubes(n):
    t = math.pow(n, 1/3)
    if ( t * t * t == n): return True
    else : return False
def check_perfect_fifth_powers(n):
    t = math.pow(n, 1/5)
    if ( t * t * t * t * t == n): return True
    else : return False

if __name__=='__main__':
    for i in range(1,1001):
        if (check_perfect_squares(i) and check_perfect_cubes(i) or check_perfect_fifth_powers(i)):
            print(i, end = " ")