#exercise 16
def o():
    ten = input("Nhập tên của bạn: ")
    phan_dau, *phan_cuoi = ten.split()
    phan_cuoi = ' '.join(phan_cuoi)

    cau_chuyen = f"Dear {ten},\n\nI am pleased to offer you our new Platinum Plus Rewards card"\
                 f" at a special introductory APR of 47.99%. {phan_dau}, an offer"\
                 f" like this does not come along every day, so I urge you to call"\
                 f" now toll-free at 1-800-314-1592. We cannot offer such a low"\
                 f" rate for long, {phan_dau}, so call right away."

    print(cau_chuyen)

if __name__ == "__main__":
    o()


