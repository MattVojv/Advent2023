import math

file = open("InputTwo.txt", "r")
inList = file.readlines()

#for line in inList:
#    print(line)


def findNum(line):
    for char in line:
        if  '0' <= char <= '9':
            return char

def replaceNumString(line):
    nums = [ "zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index = math.inf
    word = None
    for i,num in enumerate(nums):
        temp = line.find(num)
        if  -1 < temp:
            if temp < index:
                index = temp
                word = (i, num)
    if index != math.inf:
        line = line[0:index] + str(word[0]) + line[index + len(word[1]):]
    return line

    
def replaceNumString_r(line):
    #these are the reversed strings for each digit
    nums = [ "orez","eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    index = math.inf
    word = None
    for i,num in enumerate(nums):
        temp = line.find(num)
        if  -1 < temp:
            if temp < index:
                index = temp
                word = (i, num)
    if index != math.inf:
        line = line[0:index] + str(word[0]) + line[index + len(word[1]):]
    return line
    

total = 0
for line in inList:
    current = findNum(replaceNumString(line)) + findNum(replaceNumString_r(line[::-1]))
    total += int(current)

print(total)
