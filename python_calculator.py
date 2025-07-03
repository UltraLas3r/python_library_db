
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

