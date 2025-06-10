def main (): 
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, /, *): ")
    result = 0

    try:
        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "/":
            result = n1 / n2
        elif op == "*":
            result = n1 * n2
        print(f"result = {result}")
    except ValueError:
        print ("Invalid input")
        return
    except ZeroDivisionError:
        print ("Division by zero is not allowed")
        return


if __name__ == "__main__":
    main()