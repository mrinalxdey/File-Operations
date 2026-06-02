# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     if y == 0:
#         return "DivideByZeroError"
#     else:
#         return x/y

# print("Select Operation: ")
# print(''' 
#         1. Add
#         2. Subtract
#         3. Multiply
#         4. Divide''')

# choice = int(input("Enter your choice using the number: "))

# if choice in [1,2,3,4]:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == 1:
#             print("Result: ", add(num1, num2))
#         elif choice == 2:
#             print("Result: ", subtract(num1, num2))
#         elif choice == 3:
#             print("Result: ", multiply(num1, num2))
#         elif choice == 4:
#             print("Result: ", divide(num1, num2))
#     except ValueError:
#         print("Invalid Input")
# else:
#     print("Invalid Choice")

print("Calculator... enter your expression: ")
result = eval(input())
print(result)