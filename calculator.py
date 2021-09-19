# author: proobs
multi, add, sub, div = False, False, False, False


print("python calculator!\n")

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
op = input("Operator: ")

if op == "*":
    multi = True
elif op == "+":
    add = True
elif op == "-":
    sub = True
elif op == "/": 
    div == True
else:
    print("Unknown operator. Allowed operators are *, +, -, /")
    exit()


print("Generating a solution...")

if multi == True:
    answer = num1 * num2
elif add == True: 
    answer = num1 + num2
elif sub == True:
    answer = num1 - num2
elif div == True: 
    answer = num1 / num2

print(answer)