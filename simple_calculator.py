
import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")

# Jenkins se values aayengi
choice = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if choice == "1":
    print("Result:This is Add operation:", add(num1, num2))
elif choice == "2":
    print("Result:This is Sub operation:", subtract(num1, num2))
elif choice == "3":
    print("Result:This is Multiplecation operation:", multiply(num1, num2))
elif choice == "4":
    print("Result:This is Division operation:", divide(num1, num2))
else:
    print("Invalid choice")
