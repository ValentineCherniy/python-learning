def main (): 
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    op = input("Enter operation (+, -, /, *): ")
    res = 0
    result = 0

    try:
        res = float(result)
    except ValueError:
        print ("Invalid input")
        return
    except ZeroDivisionError:
        print ("Division by zero is not allowed")
        return
    
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "/":
        result = n1 / n2
    elif op == "*":
        result = n1 * n2
    print(f"result = {res}")


if __name__ == "__main__":
    main()