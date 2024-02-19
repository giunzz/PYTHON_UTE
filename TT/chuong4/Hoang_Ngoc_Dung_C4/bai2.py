tem= float(input("Enter a temp: "))
k = input("Celsius or Fahrenheit (C/F): ")
if (k == 'C'): tem = tem * 9/5 + 32
else: tem = 5/9 * (tem - 32)
print("Convert temperature : ", tem)

