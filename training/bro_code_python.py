import math

# age = 25
# num_of_students = 33
#
# print(f"{num_of_students} is the number of kids in the class")
#
# print(age)
# age += 3
#
# print(age)
# print(age)
# print(age + num_of_students)
#
# print
#
# x = 3.14
# y = 2
# z = math.pi
#
# print(z)
#
# #if statements
# age = int(input("Enter ur age: "))
# if age >= 18:
#     print("You are now signed up!")
# else:
#     print("you are too young")
#
# response = input("Would u like food (Y/N)": )
#
# if response == "Y":
#
# elif response == "N":


def run_math_process(operand):
    match operand:
        case "+":
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            z = value1 + value2
        case "-":
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            z = value1 - value2
        case "*":
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            z = value1 * value2
        case "/":
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            z = value1 / value2

    print(f"The solution is {z}")


operator_choice = input("Choose a math operator (+ - * /): ")
match operator_choice:
    case "+":
        print("You choose addition")
        run_math_process('+')

    case "-":
        print("You choose subtraction")
    case "*":
        print("You choose multiplication")
    case "/":
        print("You choose division")


