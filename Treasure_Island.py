print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
choice_1 = input("You\'re at a crossroad, where do you want to go?"
                 "Type left or right.").lower()
if choice_1 == "left":
    choice_2 = input("You\'ve come to a lake."
                     "There is an island in the middle of the of the lake."
                     'Type "wait" to wait for a boat.'
                     'Type "swim" to swim across.').lower()
    if choice_2 =="wait":
        choice_3 = input("You arrive at the island unharmed."
                         "There is house with 3 doors. One red,"
                         "Which color do you choose?").lower()
        if choice_3=="red":
            print("It's a room full of fire. Game Over.")
        elif choice_3=="blue":
            print("You enter a room of beasts. Game Over.")
        elif choice_3=="yellow":
            print("You found the treasure. You Win!")
        else:
            print("You choose a door that does'nt exist. Game Over.")
    else:
        print("you got attacked by an angry evil. Game Over.")
else:
    print("You fell in to a hole. Game Over.")