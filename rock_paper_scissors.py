import random

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images=[rock,paper,scissors]

user_choice = int(input('What do you choose? Type 0 for rock, 1 for paper, 2 for Scissor.\n'))

if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)

print(f"Computer Choice:")
print(game_images[computer_choice])
if user_choice>=3 and user_choice<0:
    print("You typed a invalid number. You lose!")
elif user_choice==0 and computer_choice==2:
    print("You Win!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif user_choice == computer_choice:
    print("It's a draw!")



