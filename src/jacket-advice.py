def main ():
    temp_input = input ("What is the temperature outside? ").strip()
    jacket_input = input ("Do you want to wear a jacket? (yes/no) ").strip().lower()

    try:
        temperature = float(temp_input)
    except ValueError:
        print ("Invalid input. Please enter a valid number of the temperature.")
        return
    
    if temperature < 10 and jacket_input == "yes":
        print ("It's cold outside. Good choice waering a jacket.")
    elif temperature >= 10 and jacket_input == "no":
        print ("That's fine. It's warm enough outside to not wear a jacket.")
    elif temperature < 10 and jacket_input == "no":
        print ("It's cold outside. You might regret not wearing a jacket.")
    elif temperature >= 10 and jacket_input == "yes":
        print ("It's quite warm. You probably don't need a jacket.")
    else:
        print ("Unexpected input. Please try again.")
if __name__ == "__main__":
    main()