import math
class tamgiac:
    def __init__(self, a , b, c, mau): 
            self.__canh1 = a 
            self.__canh2 = b
            self.canh3 = c
            self.__mau = mau
    def geta(self):
        return self.__canh1
    def getb(self):
        return self.__canh2
    def getc(self):
        return self.canh3
    def getm(self):
        return self.__mau
    def getCV(self):
        return self.__canh1 + self.__canh2 + self.canh3
    def getDT(self):
        p = self.getCV()/2
        return (p*(p-self.__canh1)*(p-self.__canh2)*(p-self.canh3))**0.5
    def hienthi(self):
        print("Thong tin ve tam giac")
        print("Canh 1: ", self.__canh1)
        print("Canh 2: ", self.__canh2)
        print("Canh 3: ", self.canh3)
        print("Mau: ", self.__mau)
        print("Chu vi: ", self.getCV())
        print("Dien tich: ", self.getDT())
    def typetamgia(self):
        if self.__canh1 == self.__canh2 == self.canh3:
            print("Tam giac deu")
        elif self.__canh1 == self.__canh2 or self.__canh1 == self.canh3 or self.__canh2 == self.canh3:
            if self.__canh1**2 + self.__canh2**2 == self.canh3**2 or self.__canh1**2 + self.canh3**2 == self.__canh2**2 or self.__canh2**2 + self.canh3**2 == self.__canh1**2:
                print("Tam giac vuong can")
            else : print("Tam giac can")
        elif self.__canh1**2 + self.__canh2**2 == self.canh3**2 or self.__canh1**2 + self.canh3**2 == self.__canh2**2 or self.__canh2**2 + self.canh3**2 == self.__canh1**2:
            print("Tam giac vuong")
        else:
            print("Tam giac thuong") 
tamgiac = tamgiac(2, 2, 5, "xanh")
tamgiac.hienthi()
tamgiac.typetamgia()