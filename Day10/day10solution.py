text = ((open("day10.txt")).read()).split("\n")

new = []
clock = 0 
x = 1 
checkpoints = [20, 60, 100, 140, 180, 220]
screen = [[], [], [], [], [], []]
global signalStrength 
signalStrength = 0

for i in range(len(text)):
    if text[i].startswith("addx"):
        var = str(text[i]).split(" ")
        new.append(var)
    elif text[i].startswith("noop"):
        new.append("0")

def signalStrengthCheck():
    if clock in checkpoints:
        currStrength = (x * clock)
        global signalStrength
        signalStrength += currStrength

global position
global rowCount
    
position = 0
rowCount = 0


def printAndSignalStrengthCheck():

    global position
    global rowCount   

    if clock in checkpoints:
        currStrength = (x * clock)
        global signalStrength
        signalStrength += currStrength
    
    global spritePos 
    spritePos = [x-1, x, x+1] #starts as 0, 1, 2

    if position in spritePos: #starts as 1, so true 
        screen[rowCount].append("#")
        position += 1
    else:
        screen[rowCount].append(".")
        position += 1
    if (clock) % 40 == 0:
        rowCount += 1
        position = 0  
    

for i in range(len(new)):
    if new[i][0] == "addx":
        clock += 1
        printAndSignalStrengthCheck()
        clock += 1 
        printAndSignalStrengthCheck()
        x += int(new[i][1])
    elif new[i][0] == "0":
        clock += 1
        printAndSignalStrengthCheck()


for i in range(len(screen)):
    screen[i]= ''.join([str(item) for item in screen[i]])




print("Signal Strength: " + str(signalStrength))
print('')
print(screen[0])
print(screen[1])
print(screen[2])
print(screen[3])
print(screen[4])
print(screen[5])




