import re
text = open("ethan11.txt").read()
text = text.split("\n\n")

# Assign Regular Expressions
origin_monkey_regex = re.compile(r'^Monkey (\d):')
starting_items_regex = re.compile(r'Starting items: ([\d,\ ]*)')
operation_regex = re.compile(r'Operation: new = old ([\+\-\*\/]) (\d+|\w+)')
test_regex = re.compile(r'Test: divisible by (\d+)')
true_regex = re.compile(r'If true: throw to monkey (\d+)')
false_regex = re.compile(r'If false: throw to monkey (\d+)')

def run_monkeys():
    monkey_array = []
    global LEAST_COMMON_MULTIPLE
    LEAST_COMMON_MULTIPLE = 1
    for monkey in text:
        if origin_monkey_regex.search(monkey):
            origin_monkey = origin_monkey_regex.search(monkey)
            starting_items = starting_items_regex.search(monkey)
            starting_items_list = str(starting_items.groups()[0]).split(", ")
            operation = operation_regex.search(monkey)
            test = test_regex.search(monkey)
            LEAST_COMMON_MULTIPLE *= int(test.group(1))
            true = true_regex.search(monkey)
            false = false_regex.search(monkey)
            monkey = Monkey(origin_monkey.group(1), starting_items_list, operation.groups(), test.group(1), true.group(1), false.group(1))
            monkey_array.append(monkey)
    print(LEAST_COMMON_MULTIPLE)
    for i in range(0, 10000):
        print("Start of round {}".format(i))
        for monkey in monkey_array:
            receiver = monkey.inspect_first_item()
            while receiver != -1:
                monkey.throw(monkey_array[receiver])
                receiver = monkey.inspect_first_item()
    inspection_array = []

    for monkey in monkey_array:
        print(repr(monkey))
        print(monkey.inspect_count)
        inspection_array.append(monkey.inspect_count)
    
    inspection_array.sort()
    print(inspection_array)
    print("Monkey Business: {}".format(inspection_array[-1] * inspection_array[-2]))

class Monkey:
    inspect_count = 0
    def __init__(self, number, items, operation, test, true, false):
        self.number = int(number)
        self.items = items
        self.operation = operation
        self.test = int(test)
        self.true = int(true)
        self.false = int(false)
    
    def __str__(self):
        return f"Monkey {self.number}: Items {self.items} Operation {self.operation}, Test {self.test}, True {self.true}, False {self.false}"
    
    def __repr__(self):
        return f"Monkey {self.number}: Items {self.items}"

    def throw(self, other_monkey):
        # print("Item of value {} thrown from monkey {} to monkey {}".format(self.items[0], self.number, other_monkey.number))
        other_monkey.receive(self.items[0])
        self.items.pop(0)
    
    def receive(self, item):
        self.items.append(item)

    def inspect_first_item(self):
        if self.items == []:
            return -1
        self.inspect_count += 1
        item = int(self.items[0])
        operand = self.operation[1]
        if operand == 'old':
            operand = int(item)
        else: 
            operand = int(self.operation[1])
        if self.operation[0] == "+":
            new_worry_level = item + operand
        elif self.operation[0] == "-":
            new_worry_level = item - operand
        elif self.operation[0] == "*":
            new_worry_level = item * operand
        elif self.operation == "/":
            new_worry_level = item / operand
        # new_worry_level //= 3
        new_worry_level %= LEAST_COMMON_MULTIPLE
        self.items[0] = new_worry_level
        if new_worry_level % int(self.test) == 0:
            return self.true
        else:
            return self.false
    
run_monkeys()