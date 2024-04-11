# Open the file
my_file = open('\\File\\file1.txt', 'r')

output = my_file.read()

r_newlines = "".join(output.splitlines())

print(r_newlines)

my_file.close()
