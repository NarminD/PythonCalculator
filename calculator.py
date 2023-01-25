value1 = float(input("Enter the first number: "))
operator = input("Enter the required operator (+, -, *, /): ")
value2 = float(input("Enter the second number: "))

if operator == "+":
    print(value1 + value2)
elif operator == "-":
    print(value1 - value2)
elif operator == "*": 
    print(value1 * value2)
elif operator == "/":
    print(value1 + value2)
else: 
    print("Entry invalid")

