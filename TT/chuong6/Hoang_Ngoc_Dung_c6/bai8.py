#exercise 8
def check_email_addresses():
    so_luong_email = int(input("Nhập số lượng địa chỉ email bạn muốn kiểm tra: "))
    dia_chi_emails = []
    for i in range(so_luong_email):
        dia_chi_email = input(f"Nhập địa chỉ email thứ {i + 1}: ")
        dia_chi_emails.append(dia_chi_email)
    la_dia_chi_sv = all("@student.college.edu" in email for email in dia_chi_emails)
    if la_dia_chi_sv:
        print("Tất cả địa chỉ email là địa chỉ email của sinh viên.")
    else:
        print("Có ít nhất một địa chỉ email của giáo sư.")

if __name__ == "__main__":
    check_email_addresses()
