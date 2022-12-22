split_text1 = ((open("day5b.txt")).read()).split("\n")
stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = [split_text1[i] for i in range(9)]

stack1 = list(stack1)
stack2 = list(stack2)
stack3 = list(stack3)
stack4 = list(stack4)
stack5 = list(stack5)
stack6 = list(stack6)
stack7 = list(stack7)
stack8 = list(stack8)
stack9 = list(stack9)

dict = {1: stack1, 2: stack2, 3: stack3, 4: stack4, 5: stack5, 6: stack6, 7: stack7, 8: stack8, 9: stack9}


split_text = ((open("day5.txt")).read()).split("\n")

for i in range(len(split_text)):
    tempmove = []
    line = split_text[i].split(" ")

    amountFromStack = int(line[1])
    originStackNum = int(line[3])
    destStack = int(line[5])
   
    for key, value in dict.items():
        if key == originStackNum:
            originStack = value

    tempmove = originStack[-amountFromStack:]
    originStack = originStack[:-amountFromStack]
    # print(originStack)
    destStack = dict[destStack]
    destStack.extend(tempmove)
    
    
    # print(originStack)
    # print(amountFromStack)
    # print(destStack)

 
print( "\n", stack1, "\n", stack2, "\n", stack3, "\n", stack4, "\n", stack5, "\n", stack6, "\n", stack7, "\n", stack8, "\n", stack9)