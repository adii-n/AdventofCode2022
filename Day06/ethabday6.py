UNIQUE_CHARACTERS_LENGTH = 14
text = open("ethan6.txt").read()

def is_unique(input_list):
    for i in range(0, len(input_list)):
        new_list = input_list.copy()
        new_list.pop(i)
        if input_list[i] in new_list:
            return False
    return True

for i in range(UNIQUE_CHARACTERS_LENGTH,len(text)+1):
    char_list = list(text[i-UNIQUE_CHARACTERS_LENGTH:i])
    if is_unique(char_list):
        print("{} characters parsed".format(i))
        break