# The 'for'-loop

# Program to find the sum of all numbers stored in a list
# List
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iteration 'for'-loop
for val in numbers:
    sum = sum + val

print("The sum is", sum)

# the range function
# side-tracking???

print(range(10))
print(list(range(10)))
print(range(2, 8))
print(list(range(2, 8)))
print(range(2, 20, 3))
print(list(range(2, 20, 3)))

# indexting using len()
print("The len() function for indexing")

genre = ['pop', 'rock', 'jazz']

# iteration using index
for i in range(len(genre)):
    print("I like", genre[i])

# for with else
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")
