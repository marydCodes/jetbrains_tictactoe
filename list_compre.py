# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [x for x in numbers if x < 5]
greater_than_5 = [x for x in numbers if x > 5]

# printing your results
print(less_than_5)
print(greater_than_5)

################################################

numstring = str(input())

oddlist = []
for char in numstring:
    num = int(char)
    if num % 2 == 1:
        # num is odd
        oddlist.append(num)
print(oddlist)

#################################################

n = int(input())

my_list = []
for i in range(n):
    my_list.append([1, 2])
print(my_list)

# list comprehension
my_list2 = [[1, 2] for i in range(n)]
print(my_list2)

#################################################

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
length = int(input())

new_list = []
for item in text:
    for x in item:
        if len(x) <= length:
            new_list.append(x)
print(new_list)

new_list2 = [x for item in text for x in item if len(x) <= length]
print(new_list2)