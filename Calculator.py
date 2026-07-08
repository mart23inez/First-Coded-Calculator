# First project being a calculator

while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Error: not a valid number!")

while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Error: not a valid number!")


print("Operations")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")



while True:
    operation = input("Enter an operation: ")
    if operation == "1" or operation == "2" or operation == "3" or operation == "4":
        break
    else:
        print("Error: not a valid operation!")


if operation == "1":
    result = num1 + num2
    print(result)
elif operation == "2":
    result = num1 - num2
    print(result)
elif operation == "3":
    result = num1 * num2
    print(result)
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Error: Cannot divide by zero")

# This project took me all of 2 days to complete. (more like two 4hr sessions.)
# I used the body of u/RockPhily's calculator code as an outline to make my own.
# Improvements over the original:
# - Input validation on both numbers using try/except (ValueError), so
#   non-numeric input (e.g. "banana") no longer crashes the program.
# - while/break loops that re-prompt until the user enters valid input.
# - Operation menu validated against allowed choices (1-4) before use.
# - Divide-by-zero guard so division by 0 is caught instead of crashing.
# - Specific exception handling (except ValueError) rather than a bare except,
#   so unexpected errors still surface instead of being silently swallowed.




