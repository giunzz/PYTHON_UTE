#exercise 15
def cl():
    lop_hoc = input("Nhập tên một lớp học: ")
    tinh_tu = input("Nhập một tính từ: ")
    hoat_dong = input("Nhập một hoạt động: ")
    cau_chuyen = f"Lớp học {lop_hoc} thật sự {tinh_tu} hôm nay. Chúng tôi học cách {hoat_dong} trong lớp học. Không thể chờ đến lớp học ngày mai!"
    print(cau_chuyen)

if __name__ == "__main__":
    cl()

