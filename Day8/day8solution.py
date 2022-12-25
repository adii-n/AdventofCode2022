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

# print(text)

edgeLength = len(text[0])


vertical = np.array(text)
vertical = vertical.reshape(-1,order = 'F')
vertical = vertical.reshape(edgeLength,edgeLength)

counter = (4*edgeLength)-4

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
        
    
print(counter)
print(scenicScore)

# # # 30373
# # # 25512
# # # 65332
# # # 33549
# # # 35390


