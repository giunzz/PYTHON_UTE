def LastNlines(fname, N):
	with open(fname) as file:
		for line in (file.readlines() [-N:]):
			print(line, end ='')
if __name__ == '__main__':
    print(1)
    fname = 'File/file1.txt'
    x = int(input("Enter the line (from 1 -> 3: )"))
    N = x
    try:
        LastNlines(fname, N)
    except:
        print('File not found')
