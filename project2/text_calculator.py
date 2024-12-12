# Text Calculator
def get_number(n):
    while True:
        operand = input(f"Number{n}: ")
        try:
            return float(operand)
        except:
            print("Invalid Number, try again!")

operand1 = get_number(1)
operand2 = get_number(2)
operation = input("Operation sign(+,-,/,*,**,%): ")

result = 0

if operation == "+":
    result = operand1 + operand2
elif operation == "-":
    result = operand1 - operand2
elif operation == "/":
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Division by zero.")
elif operation == "*":
    result = operand1 * operand2
elif operation == "**":
    result = operand1 ** operand2
elif operation == "%":
    result = operand1 % operand2
else:
    print("Invalid operation!")

print(f"Output: {result}")