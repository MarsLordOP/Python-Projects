def calculator(num1, num2, func):
    if(func == "add"):
        print(num1 + num2)
    elif(func == "sub"):
        print(num1-num2)
    elif(func == "mult"):
        print(num1 * num2)
    elif(func == "div"):
        print(num1 / num2)

calculator(10, 23, "div")