#3.1 List of Operation
fav_food=["bagel", "matcha", "salmon","cereal", "pasta"]

print(fav_food[1])
print(fav_food[-1])

fav_food.insert(0, "apple")
print(fav_food)

del fav_food[2]
print(fav_food)

print(len(fav_food))


print("Uppercase:")
for food in fav_food:
    print(food.upper())

first_and_last =[fav_food[0], fav_food[-1]]
print(first_and_last)

if "potato" in fav_food:
    print("A potato!")
else:
    print("No potato!")


#Silicing and Striding
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list=lst[::-1]
    return reversed_list[::3]

step1=get_first_15(numbers)
print(step1)
step2=get_every_5th(step1)
print(step2)
step3=reverse_and_stride(step2)
print(step3)


##3.3 Nested Lists
numbers=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[0])
print(numbers[1][1])

"""
Error: "TypeError: list indices must be integers or slices, not tuple"
How did you fix it: removing a comma I accidentally wrote
"""
numbers.append([10, 11, 12])
print(numbers)

"""
Error:TypeError: 'builtin_function_or_method' object is not subscriptable
How did you fix it: I accidentally put a square brackets instead of a parenthesis
"""

def sum_nested(lst):
    total =0
    for row in lst:
        total += sum(row)
    return total

print(sum_nested(numbers))


##3.4 Create 5x5 List
def create_matrix():
    matrix = []
    counter = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(counter)
            counter += 1
        matrix.append(row)
    return matrix

original_matrix = create_matrix()
print(original_matrix)

def replace_multiples_of_3(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for number in row:
            if number % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(number)
        new_matrix.append(new_row)
    return new_matrix  


"""
Problem: IndentationError: expected an indented block after 'if' statement on line 100
How was it fixed, I checked the the loops and how the intendation goes
"""
modified_matrix = replace_multiples_of_3(original_matrix)
print(modified_matrix)

##Dictionaries
ages={
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"])
ages["Mariam"] =100
print(ages)
ages["Milana"]="52"
print(ages)
del (ages)["Mariam"]
print(ages)

for name, age in ages.items():
    print(ages)


##FAVORITE FUNCTION
ages={
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"])
ages["Mariam"] =100
print(ages)
ages["Milana"]="52"
print(ages)
del (ages)["Mariam"]
print(ages)

for name, age in ages.items():
    print(ages)