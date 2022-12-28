text = open("ethan7.txt").read()
# text = open("ethan7test.txt").read()
text = text.split("\n")
# text = text[0:30]
text = [x.split(" ") for x in text]

size_dict = {}

def list_sum(key):
    total_sum = 0
    for element in size_dict[key]:
        if type(element) == str:
            total_sum += list_sum(element)
        else:
            total_sum += element
    return total_sum

current_path = "~"
current_dir_index = 0
while current_dir_index < len(text):
    # print("i: {}".format(current_dir_index))
    line = text[current_dir_index]
    if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
        current_dir_name = line[2]
        if current_dir_name != '/':
            current_path += '/' + current_dir_name
        current_dir_aggregate_file_size = 0
        size_dict[current_path] = []
        j = current_dir_index + 1
        while j < len(text):
            # print("j: {}".format(j))
            next_line = text[j]
            if next_line[0] == '$' and next_line[1] == 'ls':
                j += 1
                continue
            if next_line[0] == 'dir':
                size_dict[current_path].append(current_path + '/' + next_line[1])
                j += 1
                continue
            if next_line[0].isnumeric():
                current_dir_aggregate_file_size += int(next_line[0])
                j += 1
                continue
            if next_line[0] == '$':
                break
        size_dict[current_path].append(current_dir_aggregate_file_size)
        current_dir_index = j
    if line[2] == '..':
        split_path = current_path.split('/')
        current_path = '/'.join(split_path[0:-1])
        current_dir_index += 1

# print(size_dict)

complete_size_dict = {}
for key in size_dict:
    complete_size_dict[key] = list_sum(key)

# print(complete_size_dict)

less_than_100k_sum = 0

for key in complete_size_dict:
    if complete_size_dict[key] <= 100000:
        # print(key, complete_size_dict[key])
        less_than_100k_sum += complete_size_dict[key]
# print(less_than_100k_sum)

current_free_space = 70000000 - complete_size_dict['~']
space_needed = 30000000 - current_free_space
print(space_needed)

directory_sizes_that_work = []

for key in complete_size_dict:
    if complete_size_dict[key] >= space_needed:
        directory_sizes_that_work.append(complete_size_dict[key])
        
directory_sizes_that_work.sort()
print(directory_sizes_that_work[0])
