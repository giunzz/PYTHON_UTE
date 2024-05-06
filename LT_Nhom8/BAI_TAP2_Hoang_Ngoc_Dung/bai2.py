class hinhtron:
    def __init__(self, r):
        self.r = r
    def chuvi(self):
        return 2*3.14*self.r
    def dientich(self):
        return 3.14*self.r*self.r
    def hienthi(self):
        print("Thong tin cua hinh tron: ")
        print("Ban kinh: ", self.r)
        print("Chu vi: ", self.chuvi())
        print("Dientich: ", self.dientich())
    
hinhtron = hinhtron(3)
hinhtron.hienthi()