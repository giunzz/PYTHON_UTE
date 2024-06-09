# import math
# class tamgiac:
#     def __init__(self, a , b, c, mau): # phương thức khởi tạo 
#             self.__canh1 = a 
#             self.__canh2 = b
#             self.canh3 = c
#             self.__mau = mau
#     def is_triangle(self,a, b, c):
#     # Kiểm tra điều kiện tổng độ dài hai cạnh bất kỳ lớn hơn cạnh còn lại
#         if a + b > c and a + c > b and b + c > a:
#             return True
#         else:
#             return False
#     def geta(self):
#         return self.__canh1
#     def getb(self):
#         return self.__canh2
#     def getc(self):
#         return self.canh3
#     def getm(self):
#         return self.__mau
#     def getCV(self):
#         return self.__canh1 + self.__canh2 + self.canh3
#     def getDT(self):
#         p = self.getCV()/2
#         return (p*(p-self.__canh1)*(p-self.__canh2)*(p-self.canh3))**0.5
#     def hienthi(self):
#         print("Thong tin 3 cạnh")
#         print("Canh 1: ", tamgiac.geta()) # gọi hàm
#         print("Canh 2: ", self.__canh2) #<tên_biến_đối_tượng>.__class__<tên thuộc tính>
#         print("Canh 3: ", self.canh3)
#         if (self.is_triangle(self.__canh1, self.__canh2, self.canh3)):
#             print("Tam giac hop le")
#             print("Mau: ", self.__mau)
#             print("Chu vi: ", self.getCV())
#             print("Dien tich: ", self.getDT())
#             tamgiac.typetamgia() # gọi hàm
#         else : print("Khong hợp lệ")
#     def typetamgia(self):
#         if self.__canh1 == self.__canh2 == self.canh3:
#             print("Tam giac deu")
#         elif self.__canh1 == self.__canh2 or self.__canh1 == self.canh3 or self.__canh2 == self.canh3:
#             if self.__canh1**2 + self.__canh2**2 == self.canh3**2 or self.__canh1**2 + self.canh3**2 == self.__canh2**2 or self.__canh2**2 + self.canh3**2 == self.__canh1**2:
#                 print("Tam giac vuong can")
#             else : print("Tam giac can")
#         elif self.__canh1**2 + self.__canh2**2 == self.canh3**2 or self.__canh1**2 + self.canh3**2 == self.__canh2**2 or self.__canh2**2 + self.canh3**2 == self.__canh1**2:
#             print("Tam giac vuong")
#         else:
#             print("Tam giac thuong") 
# tamgiac = tamgiac(6, 3, 5, "xanh") # gọi class
# tamgiac.hienthi()



class MyClass:
  def __init__(self, *a):
    self.data = a

  def print_data(self):
    print(self.data) # (1, 2, 3, 4, 5)

# Tạo đối tượng và truyền nhiều đối tượng
obj = MyClass(1, 2, 3, 4, 5)

# Gọi phương thức
obj.print_data()
