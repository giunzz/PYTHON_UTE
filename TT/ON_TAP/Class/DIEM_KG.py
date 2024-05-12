class khong_gian():
    def __init__(self, x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def hienthi(self):
        print("Thong tin cua khong gian: ")
        print("Toa do x: ", self.x)
        print("Toa do y: ", self.y)
        print("Mau sac: ", self.color)
    def tinhTienX(self):
        self.x += self.x
        self.y += self.x
        return self.x, self.y
    def tinhTienXY(self):
        self.x += self.x
        self.y += self.y
        return self.x, self.y
    def khoangcach(self):
        return (self.x**2 + self.y**2)**0.5

khong_gian = khong_gian(3, 4, "xanh")
khong_gian.hienthi()
print("khoang cach: ", khong_gian.khoangcach())
    