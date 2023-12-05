file = open("Input.txt", "r")
game = file.readlines()

RGBmax = [12, 13, 14]
maxR = 0
maxG = 0
maxB = 0
gameSum = 0
powerSum = 0
for line in game:
    maxR = 0
    maxB = 0
    maxG = 0
    line = line.replace("\n", "")
    rounds = line.split(": ")[1].split("; ")

    for blocks in rounds:
        colour = blocks.split(", ")

        for count in colour:
            current = count.split(" ")
            if  current[1] == "blue" and int(current[0]) > maxB:
                maxB = int(current[0])
            if  current[1] == "red" and int(current[0]) > maxR:
                maxR = int(current[0])
            if  current[1] == "green" and int(current[0]) > maxG:
                maxG = int(current[0])

    temp = int(line.split(": ")[0].split(" ")[1])
    if maxR <= RGBmax[0] and maxG <= RGBmax[1] and maxB <= RGBmax[2]:
        #print(str(temp) + "-Red:" +str(maxR) + ", Blue:" + str(maxB) +", Green:" + str(maxG))
        gameSum += temp
        powerSum += maxR * maxG * maxB
    else:
        #print(str(temp) + "-NO ")
        powerSum += maxR * maxG * maxB
        #print("Red:" +str(maxR) + ", Blue:" + str(maxB) +", Green:" + str(maxG))
 

print("Game Sum is %d " %gameSum)
print("Power Sum is %d " % powerSum)
