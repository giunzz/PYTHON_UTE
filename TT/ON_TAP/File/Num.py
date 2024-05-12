# Viết chương trình Python ghi các số nguyên có giá trị từ 1 đến 
# 10 vào tệp văn bản data71.txt, mỗi số trên một dòng.

# f = open('data.txt', mode='w', encoding='utf–8') 
# for i in range(1,11):
#     f.write(str(i)+ ' ')
# f .close()

#out
# f = open('data.txt', mode='r', encoding='utf–8')
# lines = f.readline()
# print(lines) 

#sum
f = open('data.txt', mode='r', encoding='UTF-8')
lines = f.readline()
f.close()
s = 0
for i in lines:
    if i == " ": continue
    s += int(i)
    print(int(i))

file = open('data.txt', mode='a', encoding='utf-8')
file.writelines("\n"+str(s))
file.close()