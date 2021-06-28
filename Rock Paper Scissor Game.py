import random

print("**** ROCK PAPER SCISSOR GAME ****")
name = input("Enter Your Name: ")
comp_score = 0
user_score = 0
no_of_turns = 1

no_of_time = int(input("How many times you play this game:"))
print("0 or r or R for Rock\n1 or p or P for Paper\n2 or s or S for Scissor: ")

for _time in range(no_of_time):
    print(f"\n**** Turn {no_of_turns} ****")
    user_choice = input()
    comp_choice = random.randint(0, 2)
    if user_choice == comp_choice:
        print(f"Tie, {name} and Computer have same input")

    # If user select rock(0)
    elif (user_choice == "0" or "r" or "R") and comp_choice == 1:
        comp_score = comp_score + 1
        print("Computer wins 1 Point")

    elif (user_choice == "0" or "r" or "R") and comp_choice == 2:
        user_score = user_score + 1
        print(f"{name} wins 1 Point")

    # If user select paper(1)
    elif (user_choice == "1" or "p" or "P") and comp_choice == 2:
        comp_score = comp_score + 1
        print("Computer wins 1 Point")

    elif (user_choice == "1" or "p" or "P") and comp_choice == 0:
        user_score = user_score + 1
        print(f"{name} wins 1 Point")

    # If user select scissor(2)
    elif (user_choice == "2" or "s" or "S") and comp_choice == 0:
        comp_score = comp_score + 1
        print("Computer wins 1 Point")

    elif (user_choice == "2" or "s" or "S") and comp_choice == 1:
        user_score = user_score + 1
        print(f"{name} wins 1 Point")

    else:
        print("Please Enter Correct Input")
    
    no_of_turns = no_of_turns + 1

print("GAME OVER!!!")
print(f"{name} score is {user_score} and computer score is {comp_score}")
if user_score == comp_score:
    print("Game Drawn")

elif user_score > comp_score:
    final_score = user_score - comp_score
    print(f"{name} wins by {final_score}")

else:
    final_score = comp_score - user_score
    print(f"Computer wins by {final_score}")