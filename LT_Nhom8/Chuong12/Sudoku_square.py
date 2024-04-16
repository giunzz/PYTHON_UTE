import numpy as np

def check_sudoku(a):
    for i in range(9):
        j,k = (i//3) * 3 , (i%3) * 3
        if len(set(a[i,:])) != 9 or len(set(a[:,i])) != 9 or len(set(a[j:j+3,k:k+3].ravel())) != 9:
            return False
    return True

if __name__ == '__main__':
    sudoku =  """145327698
    839654127
    672918543
    496185372
    218473956
    753296431
    367542819
    984761235
    521839764"""
    line = 9
    a = np.array([[int(i) for i in line] for line in sudoku.split()])
    print(a)
    if (check_sudoku(a)): print("This is a valid sudoku")
    else: print("This is not a valid sudoku")