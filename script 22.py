# While loop
# ----------
# as long as the test condition is true

# Adding numbers
# from a user

n = int(input("Enter a value for n: "))

# initialization for sum and counter (i)
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1 #update counter --> after counter is used

print("The sum is", sum) # Prints only the result of the iterations

# While else?

counter = 0

while counter < 3:
    print("Inside loop") # It will print every iteration
    counter = counter + 1
else:
    print("Inside else")
