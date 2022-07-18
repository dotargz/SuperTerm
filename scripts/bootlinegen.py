
fileobj = open("boot.txt")
lines = []
for line in fileobj:
    lines.append(line.strip())

# open file in write mode
with open("bootlist.txt", 'w') as fp:
    fp.write(str(lines))
    print('Done')

