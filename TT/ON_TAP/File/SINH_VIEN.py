""" Chương trình nhập vào một danh sách sinh viên của một lớp, hiển thị ra 
màn hình danh sách sinh viên vừa nhập. Biết rằng mỗi sinh viên gồm các 
thông tin: Mã sinh viên, Họ tên, Lớp, Quê quán. 
"""
# nhớ CD DÔ floder

# file = open('SinhVien.txt','a', encoding='utf-8') 
# #Nhập danh sách sinh viên từ bàn phím 
# while(True): 
#     maSV = input("Mã sinh viên: ") #B2 
#     if maSV=="":  #B3 
#         break 
#     tenSV = input("Tên sinh viên: ") #B4 
#     Lop = input("Lớp: ")  # B5 
#     QueQuan = input("Quên quán: ")  # B6 
# # Ghi dữ liệu vào file 
# file.write('\t'.join([maSV, tenSV,Lop, QueQuan])+'\n')  
# file.close() 
# #B8 Hiển thị danh sách sinh viên ra màn hình 
# print('Danh sách sinh viên vừa nhập') 
# print('\t'.join(['Mã SV', 'Họ tên SV', ' Lớp ', 'Quê quán'])) 
# file = open('SinhVien.txt','r', encoding='utf-8') 
# for sv in file.readlines(): 
#     print(sv)

# input
    
# f = open('sinhvien.txt', mode='w', encoding='utf–8') 
# f .writelines(['Đường vô xứ Huế loanh quanh\n', 'Non xanh nước biếc như tranh hoạ đồ.']) 
# f .close()


#out
file = open('sinhvien.txt', mode='r', encoding='utf–8') 
lines = file.readlines()
print(lines) 
# for line in lines: print(line) 
file .close() 