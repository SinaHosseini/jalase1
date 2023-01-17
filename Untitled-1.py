import math

print("available operation is")
print("+ , - , * , / , square , sin , cos , tan , cotan , factorial")

op = input("enter your operation  ")

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("please enter first number  "))
    b = float(input("please enter second number  "))

else:
    a = float(input("please enter first number  "))

if op == "+":
    result = a + b

elif op == "/":
    if b != 0:
        result = a / b
    else:
        result = "can't devide by zero"

elif op == "*":
    result = a * b

elif op == "/":
    result = a / b

elif op == "square":
    if a < 0:
        print("Eror!")
    else:
        result = math.sqrt(a)

elif op == "sin":
    a = a / 180 * math.pi
    result = math.sin(a)

elif op == "cos":
    a = a / 180 * math.pi
    result = math.cos(a)

elif op == "tan":
    a = a / 180 * math.pi
    result = math.tan(a)

elif op == "cotan":
    a = a / 180 * math.pi
    a = math.tan(a)
    result = 1 / a

elif op == "factorial":
    result = math.factorial(int(a))


print(result)
