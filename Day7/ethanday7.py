text = open("ethan7.txt").read()
text = text.split("\n")
text = text[0:14]
text = [x.split(" ") for x in text]

size_dict = {}

# TODO: Change dictionary keys to be the path to the directory

def find_sum_of_list(input_list):
    # TODO: Finish function
    return

current_path = "/"
current_dir_index = 0
while current_dir_index < len(text):
    # print("i: {}".format(current_dir_index))
    line = text[current_dir_index]
    if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
        current_dir_name = line[2]
        if current_dir_name != '/':
            current_path += current_dir_name + "/"
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
                size_dict[current_path].append(next_line[1])
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
    else:
        # TODO: Handle cd .. case
        
        current_dir_index += 1

print(size_dict)