def categorize_bmi(weight, height):
    # Write code here
    bmi = weight / (height * height / 10000)
    if bmi < 18.5:
        print ("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Normal weight")
    elif 25 <= bmi <= 29.9:
        print("Overweight")
    else:
        print("Obese")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
categorize_bmi(weight,height)
