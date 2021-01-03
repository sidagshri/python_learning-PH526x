numbers = range(10)
squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# doing above via list comprehension
squares2 = [number**2 for number in numbers]
print(squares2)

# using list comprehension sum only even numbers
print(sum([x for x in range(10) if x % 2 == 0])) # same as sum([0,2,4,6,8])

# using list comprehension get list of squares for odd numbers
print([x**2 for x in range(10) if x % 2 != 0]) # [1,9,25,49,81]
