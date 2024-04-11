def binary_s(a,b):
    a.sort()
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high)//2
        if b == a[mid]:
            print('The word is found at position:',mid)
            break
        elif b < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        print('The word is not found')

if __name__ == '__main__':
    a = [i for i in input ("enter the list of words:").split()]
    print(a)
    b = input("Enter a word you want to find:")
    binary_s(a,b)

