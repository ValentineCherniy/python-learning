def main ():
    try:
        temperature = int(input("Enter temperature in Celsius: "))
        if temperature < 0:
            print("Wear a heavy coat.")
        elif 0 <= temperature <= 10:
            print("Wear a coat.")
        elif 11 <= temperature <= 20:
            print("Wear a jacket.")
        elif 21 <= temperature <= 30:
            print("Wear a t-shirt.")
        else:
            print("Stay hydrated!")
    except ValueError:
        print("Invalid input. Please enter a valid integer for temperature.")
        return
if __name__ == "__main__":
    main()