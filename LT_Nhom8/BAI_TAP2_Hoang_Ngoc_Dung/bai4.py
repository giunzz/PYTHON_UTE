class num_cal:
    def __init__(self, *nso):
        self.num = nso
    def sum(self):
        return sum(self.num)
    def trungbinh(self):
        return self.sum()/len(self.num)
    def ma(self):
        return max(self.num)
    def mi(self):
        return min(self.num)
    def hienthi(self):
        print("Tong: ", self.sum())
        print("Trung binh: ", self.trungbinh())
        print("Max: ", self.ma())
        print("Min: ", self.mi())
        
num_cal = num_cal(1, 2, 3, 4, 5)
num_cal = num_cal.hienthi()