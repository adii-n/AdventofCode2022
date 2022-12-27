import numpy as np
text = open("ethan9.txt").read()
# text  = open("ethan9test.txt").read()
text = text.splitlines()

array_height = 5000
array_width = 5000

rope_array = np.zeros((array_height, array_width), dtype=np.int)

print(rope_array)

head_coords = [2500, 2500]
one_coords = [2500, 2500]
two_coords = [2500, 2500]
three_coords = [2500, 2500]
four_coords = [2500, 2500]
five_coords = [2500, 2500]
six_coords = [2500, 2500]
seven_coords = [2500, 2500]
eight_coords = [2500, 2500]
tail_coords = [2500, 2500]
# rope_array[head_coords[0], head_coords[1]] = 'H'
rope_array[tail_coords[0], tail_coords[1]] = 1

def move_head(direction):
    global head_coords
    if direction == "U":
        head_coords[0] -= 1
    elif direction == "D":
        head_coords[0] += 1
    elif direction == "L":
        head_coords[1] -= 1
    elif direction == "R":
        head_coords[1] += 1
    # rope_array[head_coords[0], head_coords[1]] = 'H'
    update_1()

def update_1():
    # If 1 is adjacent or diagonal to head, do nothing
    if abs(head_coords[0] - one_coords[0]) <= 1 and abs(head_coords[1] - one_coords[1]) <= 1:
        return
    # Otherwise, move 1 in direction of head
    if head_coords[0] > one_coords[0]:
        one_coords[0] += 1
    elif head_coords[0] < one_coords[0]:
        one_coords[0] -= 1
    if head_coords[1] > one_coords[1]:
        one_coords[1] += 1
    elif head_coords[1] < one_coords[1]:
        one_coords[1] -= 1
    update_2()

def update_2():
    # If 2 is adjacent or diagonal to 1, do nothing
    if abs(one_coords[0] - two_coords[0]) <= 1 and abs(one_coords[1] - two_coords[1]) <= 1:
        return
    # Otherwise, move 2 in direction of 1
    if one_coords[0] > two_coords[0]:
        two_coords[0] += 1
    elif one_coords[0] < two_coords[0]:
        two_coords[0] -= 1
    if one_coords[1] > two_coords[1]:
        two_coords[1] += 1
    elif one_coords[1] < two_coords[1]:
        two_coords[1] -= 1
    update_3()

def update_3():
    # If 3 is adjacent or diagonal to 2, do nothing
    if abs(two_coords[0] - three_coords[0]) <= 1 and abs(two_coords[1] - three_coords[1]) <= 1:
        return
    # Otherwise, move 3 in direction of 2
    if two_coords[0] > three_coords[0]:
        three_coords[0] += 1
    elif two_coords[0] < three_coords[0]:
        three_coords[0] -= 1
    if two_coords[1] > three_coords[1]:
        three_coords[1] += 1
    elif two_coords[1] < three_coords[1]:
        three_coords[1] -= 1
    update_4()

def update_4():
    # If 4 is adjacent or diagonal to 3, do nothing
    if abs(three_coords[0] - four_coords[0]) <= 1 and abs(three_coords[1] - four_coords[1]) <= 1:
        return
    # Otherwise, move 4 in direction of 3
    if three_coords[0] > four_coords[0]:
        four_coords[0] += 1
    elif three_coords[0] < four_coords[0]:
        four_coords[0] -= 1
    if three_coords[1] > four_coords[1]:
        four_coords[1] += 1
    elif three_coords[1] < four_coords[1]:
        four_coords[1] -= 1
    update_5()

def update_5():
    # If 5 is adjacent or diagonal to 4, do nothing
    if abs(four_coords[0] - five_coords[0]) <= 1 and abs(four_coords[1] - five_coords[1]) <= 1:
        return
    # Otherwise, move 5 in direction of 4
    if four_coords[0] > five_coords[0]:
        five_coords[0] += 1
    elif four_coords[0] < five_coords[0]:
        five_coords[0] -= 1
    if four_coords[1] > five_coords[1]:
        five_coords[1] += 1
    elif four_coords[1] < five_coords[1]:
        five_coords[1] -= 1
    update_6()

def update_6():
    # If 6 is adjacent or diagonal to 5, do nothing
    if abs(five_coords[0] - six_coords[0]) <= 1 and abs(five_coords[1] - six_coords[1]) <= 1:
        return
    # Otherwise, move 6 in direction of 5
    if five_coords[0] > six_coords[0]:
        six_coords[0] += 1
    elif five_coords[0] < six_coords[0]:
        six_coords[0] -= 1
    if five_coords[1] > six_coords[1]:
        six_coords[1] += 1
    elif five_coords[1] < six_coords[1]:
        six_coords[1] -= 1
    update_7()

def update_7():
    # If 7 is adjacent or diagonal to 6, do nothing
    if abs(six_coords[0] - seven_coords[0]) <= 1 and abs(six_coords[1] - seven_coords[1]) <= 1:
        return
    # Otherwise, move 7 in direction of 6
    if six_coords[0] > seven_coords[0]:
        seven_coords[0] += 1
    elif six_coords[0] < seven_coords[0]:
        seven_coords[0] -= 1
    if six_coords[1] > seven_coords[1]:
        seven_coords[1] += 1
    elif six_coords[1] < seven_coords[1]:
        seven_coords[1] -= 1
    update_8()

def update_8():
    # If 8 is adjacent or diagonal to 7, do nothing
    if abs(seven_coords[0] - eight_coords[0]) <= 1 and abs(seven_coords[1] - eight_coords[1]) <= 1:
        return
    # Otherwise, move 8 in direction of 7
    if seven_coords[0] > eight_coords[0]:
        eight_coords[0] += 1
    elif seven_coords[0] < eight_coords[0]:
        eight_coords[0] -= 1
    if seven_coords[1] > eight_coords[1]:
        eight_coords[1] += 1
    elif seven_coords[1] < eight_coords[1]:
        eight_coords[1] -= 1
    update_tail()

def update_tail():
    # If tail is adjacent or diagonal to 8, do nothing
    if abs(eight_coords[0] - tail_coords[0]) <= 1 and abs(eight_coords[1] - tail_coords[1]) <= 1:
        return
    # Otherwise, move tail in direction of 8
    if eight_coords[0] > tail_coords[0]:
        tail_coords[0] += 1
    elif eight_coords[0] < tail_coords[0]:
        tail_coords[0] -= 1
    if eight_coords[1] > tail_coords[1]:
        tail_coords[1] += 1
    elif eight_coords[1] < tail_coords[1]:
        tail_coords[1] -= 1

    rope_array[tail_coords[0], tail_coords[1]] = 1

    
for line in text:
    line = line.split(" ")
    for i in range(int(line[1])):
        # print("Head starts at: " + str(head_coords))
        # print("Tail starts at: " + str(tail_coords))
        # print("Moving head " + line[0] + " " + str(i+1) + " times")
        move_head(line[0])
        # print("Head ends at: " + str(head_coords))
        # print("Tail ends at: " + str(tail_coords))
        # print(rope_array)
        # print()

positions_visited = np.count_nonzero(rope_array)
print("Positions visited: " + str(positions_visited))