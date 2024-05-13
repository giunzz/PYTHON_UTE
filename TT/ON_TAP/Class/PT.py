import math
# Giải phương trình bậc 2: ax2 + bx + c = 0
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình có nghiệm phức");
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b));
        return;
    # tính delta
    delta = b * b - 4 * a * c;
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");

def  hePT2an(a1, b1, c1 , a2 , b2 , c2):
    D = a1 * b2 - a2 * b1;
    Dx = c1 * b2 - c2 * b1;
    Dy = a1 * c2 - a2 * c1;
    if (D == 0):
        if (Dx + Dy == 0):
            print("He phuong trinh co vo so nghiem")
        else:
            print("He phuong trinh vo nghiem")
    else :
        x = Dx / D;
        y = Dy / D;
        print("He phuong trinh co nghiem", x, y)

# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "));
b = float(input("Nhập hệ số bậc 1, b = "));
c = float(input("Nhập hằng số tự do, c = "));
# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)