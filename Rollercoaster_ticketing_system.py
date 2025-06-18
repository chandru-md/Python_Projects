print("Welcome to the Rollercoaster Ticker Counter!")
height = int(input("Enter your height in cm: "))
bill = 0
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input('Enter your age: '))
    if age <= 12:
        bill = 5
        print("Children tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    elif age >18:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want photos taken? Please confirm y for Yes and n for No ")
    if wants_photo == 'y':
        print("Please pay additionally $3")
        bill +=3

    print (f"your final bill is ${bill}")
else:
    print("You are not allowed to the rollercoaster, you have to grow taller before you can ride.")
