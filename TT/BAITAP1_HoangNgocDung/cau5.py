def check_ptchan(a):
    ans = a[0]
    for i in a:
        if i % 2 == 0: ans = max(ans, i)
    return ans
def check_ptle(a):
    ans = a[0]
    for i in a:
        if i % 2 != 0: ans = max(ans, i)
    return ans

if __name__ == '__main__':
    a = []
    n = int(input("Nhap so phan tu cua list: "))
    for i in range(n):
        a.append(int(input("Nhap phan tu thu " + str(i+1) + ": ")))
    print("So chan lon nhat trong list:" , check_ptchan(a))
    print("So le lon nhat trong list:" ,check_ptle(a))

