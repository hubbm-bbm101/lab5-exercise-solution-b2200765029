import random 
number = random.randint(1,100)
your_number = int(input("Please enter a number between 1 and 100 : "))
while number != your_number:
    if your_number < number:
        print("Increase your number")
        your_number = int(input("Please enter a number between 1 and 100 : "))
    else:
        print("Decrease your number")
        your_number = int(input("Please enter a number between 1 and 100 : "))
print("your_number is equal to number. You guessed it correctly.")