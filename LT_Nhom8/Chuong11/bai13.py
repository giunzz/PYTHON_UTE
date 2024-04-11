
with open("File/x.txt") as xh:
    with open('File/y.txt') as yh:
        with open("File/z.txt","w") as zh:
            xlines = xh.readlines()
            ylines = yh.readlines()
            for i in range(len(xlines)):
                line = ylines[i].strip() + ' ' + xlines[i]
                zh.write(line)