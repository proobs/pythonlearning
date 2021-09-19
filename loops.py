i = 1
while i <= 5: 
    print(i)
    # increment by 1, since python doesn't have variable++ we use i+= 1
    i += 1
print("done")

# create the letter F using the list and a loop
numbers = [5, 2, 5, 2, 2]
length = len(numbers)

for inumber in range(length):
    print("x" * numbers[inumber])


# find the biggest number in a list using a loop and another variable
somelist = [5, 6, 7]
max = somelist[0]

for inum in somelist: 
    if inum > max:
        max = inum
print(max)