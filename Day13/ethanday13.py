import re
text = open("ethan13.txt").read()
text = text.split("\n\n")

class Packet():
    def __init__(self, packet_list):
        self.packet_list = packet_list
    def __str__(self):
        return str(self.packet_list)
    def __lt__(self, other_packet):
        return compare_packets(self.packet_list, other_packet.packet_list)
    def __eq__(self, other_packet):
        return self.packet_list == other_packet.packet_list


def compare_packets(packet1, packet2):
    # print(f"Comparing {packet1} and {packet2}")
    if type(packet1) == int and type(packet2) == int:
        # print("Both are ints")
        if packet1 == packet2:
            return None
        # print(f"Returning {packet1} < {packet2}")
        return packet1 < packet2
    elif type(packet1) == list and type(packet2) == list:
        # print("Both are lists")
        if len(packet1) == 0 and len(packet2) == 0:
            return None
        elif len(packet1) == 0:
            return True
        elif len(packet2) == 0:
            return False
        else:
            if compare_packets(packet1[0], packet2[0]) == None:
                return compare_packets(packet1[1:], packet2[1:])
            else:
                return compare_packets(packet1[0], packet2[0])
    elif type(packet1) == int and type(packet2) == list:
        # print("Packet 1 is int, packet 2 is list")
        temp_list = []
        temp_list.append(packet1)
        return compare_packets(temp_list, packet2)
    elif type(packet1) == list and type(packet2) == int:
        # print("Packet 1 is list, packet 2 is int")
        temp_list = []
        temp_list.append(packet2)
        return compare_packets(packet1, temp_list)

def create_packet(line): # line is a string
    total_packet = []
    if line == "[]":
        return total_packet
    if line[0] == "[" and line[-1] == "]":
        line = line[1:-1]
    else:
        return int(line)
    new_line = ""
    bracket_count = 0
    for char in line:
        if char == "[":
            bracket_count += 1
        elif char == "]":
            bracket_count -= 1
        if char == "," and bracket_count > 0:
            new_line += " "
            continue
        new_line += char
    line = new_line
    line = line.split(",")
    for item in line:
        item = item.replace(" ", ",")
        total_packet.append(create_packet(item))
    return total_packet

results_array = []
packet_array = []

for pair in text:
    pair = pair.split("\n")
    packet1 = create_packet(pair[0])
    packet2 = create_packet(pair[1])
    results_array.append(compare_packets(packet1, packet2))
    packet_array.append(Packet(packet1))
    packet_array.append(Packet(packet2))

packet_array.append(Packet([[2]]))
packet_array.append(Packet([[6]]))

print(results_array)
correct_indices_sum = 0
for i in range(len(results_array)):
    if results_array[i] == True:
        correct_indices_sum += (i + 1)
print(correct_indices_sum)

packet_array.sort()

for packet in packet_array:
    print(packet)

index_2 = packet_array.index(Packet([[2]])) + 1
index_6 = packet_array.index(Packet([[6]])) + 1
decoder_key = index_2 * index_6
print(index_2, index_6, decoder_key)