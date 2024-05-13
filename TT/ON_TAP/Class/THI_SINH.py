class ThiSinh:
    def __init__(self, so_bao_danh, ho_ten, diem_toan, diem_tieng_viet):
        self.so_bao_danh = so_bao_danh
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_tieng_viet = diem_tieng_viet

def nhap_danh_sach_thi_sinh():
    danh_sach_thi_sinh = []
    n = int(input("Nhập số lượng thí sinh: "))
    for i in range(n):
        so_bao_danh = input("Nhập số báo danh: ")
        ho_ten = input("Nhập họ và tên: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_tieng_viet = float(input("Nhập điểm Tiếng Việt: "))
        thi_sinh = ThiSinh(so_bao_danh, ho_ten, diem_toan, diem_tieng_viet)
        danh_sach_thi_sinh.append(thi_sinh)
    return danh_sach_thi_sinh

def hien_thi_danh_sach_thi_sinh(danh_sach_thi_sinh):
    print("\nDanh sách thí sinh:")
    for thi_sinh in danh_sach_thi_sinh:
        print(f"Số báo danh: {thi_sinh.so_bao_danh}, Họ tên: {thi_sinh.ho_ten}, Điểm Toán: {thi_sinh.diem_toan}, Điểm Tiếng Việt: {thi_sinh.diem_tieng_viet}")

def hien_thi_thi_sinh_tong_diem_lon_hon_10(danh_sach_thi_sinh):
    print("\nThí sinh có tổng điểm lớn hơn 10:")
    for thi_sinh in danh_sach_thi_sinh:
        tong_diem = thi_sinh.diem_toan + thi_sinh.diem_tieng_viet
        if tong_diem > 10:
            print(f"Số báo danh: {thi_sinh.so_bao_danh}, Họ tên: {thi_sinh.ho_ten}, Tổng điểm: {tong_diem}")

def hien_thi_thi_sinh_diem_liet(danh_sach_thi_sinh):
    print("\nThí sinh có điểm liệt:")
    for thi_sinh in danh_sach_thi_sinh:
        if thi_sinh.diem_toan == 0 or thi_sinh.diem_tieng_viet == 0:
            print(f"Số báo danh: {thi_sinh.so_bao_danh}, Họ tên: {thi_sinh.ho_ten}")

# Main program
danh_sach_thi_sinh = nhap_danh_sach_thi_sinh()
hien_thi_danh_sach_thi_sinh(danh_sach_thi_sinh)
hien_thi_thi_sinh_tong_diem_lon_hon_10(danh_sach_thi_sinh)
hien_thi_thi_sinh_diem_liet(danh_sach_thi_sinh)