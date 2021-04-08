calculator_operator = None


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def menu():
    global calculator_operator
    valid_answer = False
    print("This is a calculator")
    print("Please select an operator by choosing the number before it")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while not valid_answer:
        calculator_operator = int(input("Enter the number that corresponds to the operation you would like to do: "))

        if 0 >= calculator_operator or calculator_operator >= 5:
            print(" Invalid Input")

        else:
            valid_answer = True
            number1 = float(input("Enter First Value: "))
            number2 = float(input("Enter Second Value: "))

            if calculator_operator == 1:
                print("{0} + {1} = {2}".format(str(number1), str(number2), str(addition(number1, number2))))

            elif calculator_operator == 2:
                print("{0} - {1} = {2}".format(str(number1), str(number2), str(subtraction(number1, number2))))

            elif calculator_operator == 3:
                print("{0} * {1} = {2}".format(str(number1), str(number2), str(multiplication(number1, number2))))

            elif calculator_operator == 4:
                if number1 == 0 and number2 == 0:
                    print ("You cannot divide by 0")
                else:
                    print("{0} / {1} = {2}".format(str(number1), str(number2), str(division(number1, number2))))


def main():
    menu()


if __name__ == '__main__':
    main()
