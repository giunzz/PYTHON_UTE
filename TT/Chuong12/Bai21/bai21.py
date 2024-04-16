import re

fileToRead = 'high_temperatures.txt'
file = open(fileToRead, 'r')
listLine = file.readlines()
a = {}
cnt = 0 
for i in listLine: 
    tmp = re.findall('[0-9]+', i)
    a.update({tmp[0]:cnt})
    cnt += 1
print("Average high temperature: ",sum([int(i) for i in a.keys()])/len(a.keys()))
sorted(a.keys())
for i in a.values():
    print(listLine[i], end='')

# for i in sorted(a.keys()):
#     print(a[i], end='')