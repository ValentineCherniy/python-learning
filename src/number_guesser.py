import random
from random import randint


def main():
    random_number = random.randint(1, 100)
    input_number = 0
    print(input_number, random_number)


    while input_number != random_number:
        try:
            input_number = int(input("Input number from 1 to 100 = "))
        except ValueError:
            print("Enter the integer number!")
        if input_number != random_number:
            print("You didn't guess the number. Try again...")


    print("Congratulations! You guess the number!")


if __name__ == "__main__":
    main()
