name = input ("What is your name? ")
age = input ("What is your age? ")

print (f"Hello, {name}!")

try:
    age_int = int(age)
    print(f"In 5 years, you will be {age_int + 5} years old.")
except ValueError:
    print("Please enter a valid number for your age.")