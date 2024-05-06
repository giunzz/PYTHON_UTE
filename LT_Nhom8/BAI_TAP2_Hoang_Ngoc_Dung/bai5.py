class subject:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.credit = 0
    def nhap(self):
        print("Nhap thong tin mon hoc")
        self.id = input("Nhap ma mon hoc: ")
        self.name = input("Nhap ten mon hoc: ")
        self.credit = input("Nhap so tin chi: ")

class HocVien:
    def __init__(self):
        self.the = ""
        self.ten = ""
        self.namsinh = 0
        self.monhoc = []
        self.num = 0
    def nhap(self):
        print("Nhap thong tin sinh vien")
        self.the = input("Nhap ma sinh vien: ")
        self.ten = input("Nhap ten sinh vien: ")
        self.namsinh = input("Nhap nam sinh sinh vien: ")
        self.num = input("So mon muon dang ki: ")
        mon = []
        for i in self.num:
            monhoc = subject()
            monhoc.nhap()
            self.monhoc.append(monhoc)
            mon.append(monhoc)
    def __str__(self) -> str:
        return f"Ma sinh vien: {self.the}, Ten sinh vien: {self.ten}, Nam sinh: {self.namsinh}, Danhsachmonhoc : {self.monhoc}"

class QuanLyHocVien:
    def __init__(self):
        self.danh_sach_hv = []
        self.n = []
    def them_hoc_vien(self):
        hv = HocVien()
        hv.nhap()
        self.danh_sach_hv.append(hv)
        self.n.append(HocVien().num)

    def luu_danh_sach(self):
        with open('DSHV.txt', 'w') as f:
            for hv in self.danh_sach_hv:
                f.write(str(hv))
    def hienthi(self):
        print("Danh sach hoc vien")
        for hv in self.danh_sach_hv:
            print(hv)
        print("Danh sach hoc vien co ist nhat 2 mon hoc")
        for i in range(len(self.danh_sach_hv)):
            if self.n[i] <= 2:
                print(self.danh_sach_hv[i])

ql = QuanLyHocVien()
ql.them_hoc_vien()
ql.luu_danh_sach()
ql.hienthi()
    
    