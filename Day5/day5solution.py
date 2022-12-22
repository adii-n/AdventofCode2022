split_text1 = ((open("day5b.txt")).read()).split("\n")
stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = [split_text1[i] for i in range(9)]

# stack1, stack2, stack3 = [split_text1[i] for i in range(3)]


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

# dict = {1: stack1, 2: stack2, 3: stack3}


split_text = ((open("day5.txt")).read()).split("\n")

for i in range(len(split_text)):
    originStack = -1 ## integer value of the stack that the move is coming from
    tempmove = [] ## the move that is being made
    line = split_text[i].split(" ") ## the line of text that is being read

    amountFromStack = int(line[1]) ## the amount of blocks that are being moved
    originStackNum = int(line[3]) ## the stack that the move is coming from
    destStackNum = int(line[5]) ## the stack that the move is going to
   
    for key, value in dict.items():
        if key == originStackNum:
            originStack = value 

    tempmove = originStack[-amountFromStack:] ## the move that is being made
    tempmove = tempmove[::-1] ## ****** FOR PART 2, COMMENT THIS LINE OUT ******  
    del originStack[-amountFromStack:] ## the move that is being made
    # print(tempmove)
    for key, value in dict.items():
        if key == destStackNum:
            destStack = value 
    
    destStack.extend(tempmove)
    # print(destStack)    

print( "\n", stack1, "\n", stack2, "\n", stack3, "\n", stack4, "\n", stack5, "\n", stack6, "\n", sta    ck7, "\n", stack8, "\n", stack9)