# author: proobs

# only two parameters possible
def test1(a, b):
    return a*b

print(test1(1, 2))

# Multiple parameters are possible here
def test2(*list):
    total = 1
    for number in list:
        # total = current total * number in list
        total *= number
    return total

print(test2(1,2))

# print message formatted in keyvalue pairs
def test3(**some):
    print(some)

test3(id=1, name="somename")

# print id parameter only
# can change id to name and it'll print whatever is = to name
def test4(**some):
    print(some["id"])

test4(id=1, name="somename")

# global variables.
somevar = "a"

def test5():
    somevar = "b"

# this will only print a because in python, global varialbles cannot be changed in functions (local scope), they are completely seperate
test5()
print(somevar)

# but this works. Avoid using global variables. It is bad practice
def test6():
    global somevar
    somevar = "b"

test6()
print(somevar)


# function that looks for the biggest number in a list

testlist = [1, 2, 3, 4]
biggest_num = testlist[0]

def test7():
    global biggest_num
    for number in testlist:
        if number > biggest_num:
            biggest_num = number

test7()
print(biggest_num)

# Handling Errors

# basically, with this try and except function, you take use it to prevent programs from crashing if they encounter an expected error
# here, it basically means that if, the user tries to input anything that can cause a value error (string, float), it will instead print a message that it's an invalid value
try:
    someage = int(input('Age: '))
    print(someage)
except ValueError:
    print("Invalid value")

# These blocks can have multiple exceptions
