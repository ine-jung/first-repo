print("🧮 Welcome to the Mini Calculator!")

num1 = float(input("Enter the first number: "))
op = input("Choose an operation (+, +, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Can't devide by zero!"
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

print(f"Result: {result}")