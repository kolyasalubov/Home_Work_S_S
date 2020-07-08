num1 =float(input("Enter the number: "))
num =input("Select an action! (+, -, /, *, **, //, %): ")
num2 =float(input("Enter the number: "))
num3 = ("Result")
if num == "+":
    print(num3, num1 + num2)
elif num == "-":
    print(num3, num1 - num2)
elif num == "/":
    print(num3, num1 / num2)
elif num == "*":
    print(num3, num1 * num2)
elif num == "**":
    print(num3, num1 ** num2)
elif num == "//":
    print(num3, num1 // num2)
elif num == "%":
    print(num3, num1 % num2)
else:
    print("Invalid character")