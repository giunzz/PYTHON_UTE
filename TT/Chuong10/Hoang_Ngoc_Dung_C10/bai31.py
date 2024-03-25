

c_not = [31,29,30,31,30,31,31,30,31,30,31,31]
c_leap = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(y):
    y = int(y)
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def cal(y):
    if is_leap_year(y[2]):
        return sum(c_leap[:int(y[0])]) + int(y[1])
    else:
        return sum(c_not[:int(y[0])]) + int(y[1])
    
if __name__ == '__main__':
    year1 = (input("Enter a year (mm/dd/yyyy): ")).split("/")
    year2 = (input("Enter a year (mm/dd/yyyy): ")).split("/")
    day1 = cal(year1)
    day2 = cal(year2)
print("Days apart: ", abs(day1 - day2))