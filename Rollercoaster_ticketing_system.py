print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter you age: "))
    if age <=18:
        print("Please pay $7 for the ticket")
    else:
        print('Please pay $12 for the ticket')
else:
    print("You are not allowed to the rollercoaster, you have to grow taller before you can ride.")
