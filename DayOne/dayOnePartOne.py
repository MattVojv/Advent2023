file = open("InputTwo.txt", "r")
inList = file.readlines()

#for line in inList:
#    print(line)


def findNum(line):
    for char in line:
        if  '0' <= char <= '9':
            return char

total = 0
for line in inList:
    current = findNum(line) + findNum(reversed(line))
    total += int(current)

print(total)