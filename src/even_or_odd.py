def main ():
    print ("This application tests if the input number is even or odd")
    try:
        number = int(input("Enter nubmer to test: "))
        if (number % 2) != 0:
            print("The nubmer is odd.")
        else:
            print("The number is even.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for number")
        return
if __name__ == "__main__":
    main()