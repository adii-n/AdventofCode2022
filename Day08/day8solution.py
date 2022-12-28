import numpy as np

text = ((open("day8.txt")).read()).split("\n")
text = [list(i) for i in text]

horizontal = ((open("day8.txt")).read()).split("\n")
horizontal = [list(i) for i in horizontal]

horizontal.pop(0)
horizontal.pop(-1)

for i in range(len(horizontal)):
    horizontal[i].pop(0)
    horizontal[i].pop(-1)


edgeLength = len(text[0])


vertical = np.array(text)
vertical = vertical.reshape(-1,order = 'F')
vertical = vertical.reshape(edgeLength,edgeLength)

counter = (4*edgeLength)-4

highestSS = 0 


for i in range(len(horizontal)):
    for x in range(len(horizontal[i])):
        
        arrLR = text[i+1]
        arrUD = vertical[x+1]
        
        left = arrLR[:(x+1)]
        right = arrLR[(x+2):]        
        up = arrUD[:(i+1)]
        down = arrUD[(i+2):]   
    
        
        if horizontal[i][x] > max(left) or horizontal[i][x] > max(right) or horizontal[i][x] > max(up) or horizontal[i][x] > max(down):
            counter += 1
        
        tree = int(horizontal[i][x])
        print(tree)
        
        leftSS = 0
        rightSS = 0
        upSS = 0
        downSS = 0
        
        localSS = 0 


        left = [int(string) for string in left]
        left = left[::-1]
        right = [int(string) for string in right]
        up = [int(string) for string in up]
        up = up[::-1]
        down = [int(string) for string in down]

        
        
        tallerOrEqual = False

        for y in range(len(left)):
            if tallerOrEqual == False:
                if tree > left[y]:
                    leftSS += 1
                if tree == left[y]:
                    tallerOrEqual = True
                    leftSS += 1
                if tree < left[y]:
                    tallerOrEqual = True
                    leftSS += 1
        
        tallerOrEqual = False
        
        for y in range(len(right)):
            if tallerOrEqual == False:
                if tree > right[y]:
                    rightSS += 1
                if tree == right[y]:
                    tallerOrEqual = True
                    rightSS += 1
                if tree < right[y]:
                    tallerOrEqual = True
                    rightSS += 1
        
        tallerOrEqual = False
        
        for y in range(len(up)):
            if tallerOrEqual == False:
                if tree > up[y]:
                    upSS += 1
                if tree == up[y]:
                    tallerOrEqual = True
                    upSS += 1
                if tree < up[y]:
                    tallerOrEqual = True
                    upSS += 1
        
        tallerOrEqual = False

        for y in range(len(down)):
            if tallerOrEqual == False:
                if tree > down[y]:
                    downSS += 1
                if tree == down[y]:
                    tallerOrEqual = True
                    downSS += 1
                if tree < down[y]:
                    tallerOrEqual = True
                    downSS += 1
        
        localSS = leftSS * rightSS * upSS * downSS
        
        if localSS > highestSS:
            highestSS = localSS

        
        print(leftSS, rightSS, upSS, downSS)
        print(localSS)
        print('')

# # # 30373
# # # 25512
# # # 65332
# # # 33549
# # # 35390

print(counter)
print(highestSS)
