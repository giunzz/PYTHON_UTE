def readEmail_A(fileToRead):
    file = open(fileToRead, 'r')
    listLine = file.readlines()

    for i in range(len(listLine)):
        if i == len(listLine) - 1:
            print(listLine[i].strip(), end='')
        else:
            print(listLine[i].strip(), end=',')

def readEmail_B(fileToRead):
    file = open(fileToRead, 'r')
    listLine = file.readlines()

    for i in range(len(listLine)):
        if ("prof.college.edu." in listLine[i].strip()): continue
        if i == len(listLine) - 1:
            print(listLine[i].strip(), end='')
        else:
            print(listLine[i].strip(), end=',')

if __name__ == '__main__':
    fileToRead = 'email.txt'
    print("print out a string consisting of those email addresses separated by semicolons.")
    readEmail_A(fileToRead)
    print("\n new string should contain only those email addresses that do not end in @prof.college.edu.")
    readEmail_B(fileToRead)
    




