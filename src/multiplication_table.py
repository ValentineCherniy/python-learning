def main():
    input_number = input("Enter a number: ")

    for i in range(10):
        try:
            number = int(input_number)
        except ValueError:
            print("Enter an integer number!")
            return
        print(f"{number} x {i + 1} = {number * (i+1)}")

if __name__ == "__main__":
    main()
