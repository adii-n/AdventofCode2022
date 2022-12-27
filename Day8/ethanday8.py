text = open("ethan8.txt").read()
# text = open("ethan8test.txt").read()
text = text.split("\n")

tree_array = []

for line in text:
    tree_line = []
    for char in line:
        tree_line.append(int(char))
    tree_array.append(tree_line)

print(tree_array)

def is_visible(tree_x, tree_y, tree_array):
    current_tree_height = tree_array[tree_y][tree_x]
    print("Checking tree (%d, %d)..." % (tree_x, tree_y))
    left_clear = True
    right_clear = True
    up_clear = True
    down_clear = True

    # Check left
    for other_x in range(0, tree_x):
        if tree_array[tree_y][other_x] >= current_tree_height:
            print("Tree at (%d, %d) is blocked on the left by tree at (%d, %d)" % (tree_x, tree_y, other_x, tree_y))
            left_clear = False
            break
    # Check right
    for other_x in range(tree_x + 1, len(tree_array[0])):
        if tree_array[tree_y][other_x] >= current_tree_height:
            print("Tree at (%d, %d) is blocked on the right by tree at (%d, %d)" % (tree_x, tree_y, other_x, tree_y))
            right_clear = False
            break
    # Check up
    for other_y in range(0, tree_y):
        if tree_array[other_y][tree_x] >= current_tree_height:
            print("Tree at (%d, %d) is blocked on the top by tree at (%d, %d)" % (tree_x, tree_y, tree_x, other_y))
            up_clear = False
            break
    # Check down
    for other_y in range(tree_y + 1, len(tree_array)):
        if tree_array[other_y][tree_x] >= current_tree_height:
            print("Tree at (%d, %d) is blocked on the bottom by tree at (%d, %d)" % (tree_x, tree_y, tree_x, other_y))
            down_clear = False
            break
    return left_clear or right_clear or up_clear or down_clear

print("Checking trees...")

visible_count = 0

for y in range(0, len(tree_array)):
    for x in range(0, len(tree_array[0])):
        if is_visible(x, y, tree_array):
            print("Tree at (%d, %d) is visible" % (x, y))
            visible_count += 1

print(visible_count)

def get_scenic_score(tree_x, tree_y, tree_array):
    current_tree_height = tree_array[tree_y][tree_x]
    print("Calculating score for tree (%d, %d)..." % (tree_x, tree_y))
    left_tree_count = 0
    right_tree_count = 0
    up_tree_count = 0
    down_tree_count = 0

    # Count left
    for other_x in reversed(range(0, tree_x)):
        left_tree_count += 1
        if tree_array[tree_y][other_x] >= current_tree_height:
            break
    # Count right
    for other_x in range(tree_x + 1, len(tree_array[0])):
        right_tree_count += 1
        if tree_array[tree_y][other_x] >= current_tree_height:
            break
    # Count up
    for other_y in reversed(range(0, tree_y)):
        up_tree_count += 1
        if tree_array[other_y][tree_x] >= current_tree_height:
            break
    # Count down
    for other_y in range(tree_y + 1, len(tree_array)):
        down_tree_count += 1
        if tree_array[other_y][tree_x] >= current_tree_height:
            break
    print("Tree at (%d, %d) can see %d trees to the left, %d trees to the right, %d trees above, and %d trees below" % (tree_x, tree_y, left_tree_count, right_tree_count, up_tree_count, down_tree_count))
    scenic_score = left_tree_count * right_tree_count * up_tree_count * down_tree_count
    return scenic_score

greatest_scenic_score = 0

for y in range(0, len(tree_array)):
    for x in range(0, len(tree_array[0])):
        current_scenic_score = get_scenic_score(x, y, tree_array)
        if current_scenic_score > greatest_scenic_score:
            greatest_scenic_score = current_scenic_score

print(greatest_scenic_score)