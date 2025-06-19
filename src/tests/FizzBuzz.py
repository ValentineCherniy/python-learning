print ("Welcome to FizzBuzz!")
def fizzbuzz (num):
    int_num = int(num)
    if (int_num % 3 == 0) and (int_num % 7 != 0):
        return "Fizz"
    elif (int_num % 7 == 0) and (int_num % 3 != 0):
        return "Buzz"
    elif (int_num % 3 == 0) and (int_num % 7 == 0):
        return "FizzBuzz"
    elif "3" in str(num):
            return "Almost Fizz"
    else:
        return num
number = input()
for i in range (1, int(number)+1):
    print (fizzbuzz(i))