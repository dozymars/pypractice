import random
pick = ["rock", "paper", "scissor"]
while True:
    player_1 = input(f"play - {pick[0]}, {pick[1]}, {pick[2]}: ")
    randy = random.randint(0, 2)
    computer = pick[randy]

    if player_1 == "rock" and computer == "paper":
        print("You Won")

    elif player_1 == "rock" and computer == "scissor":
        print("You Won")

    elif player_1 == computer:
        print("Its a tie, play again!")
        continue

    else:
        print("Computer Won!")
    break





