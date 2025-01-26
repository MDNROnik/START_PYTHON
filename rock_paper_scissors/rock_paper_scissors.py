import random

choices = ["rock", "paper" , "scissors"]

play = True
while(play):
    computer = random.choice(choices)
    print("Choose Any Of Them ")
    player = None

    while player not in choices:
        player = input(choices).lower()

    print("Computer Choose is ",computer)
    if(player==computer):
        print("Tie !!!")
    elif player=="rock":
        if(computer=="paper"):
            print("You Lose")
        else:
            print("You Win")
    elif player=="scissors":
        if(computer=="paper"):
            print("You Win")
        else:
            print("You Loss")
    elif player=="paper":
        if(computer=="scissors"):
            print("You Lose")
        else:
            print("You Win")

    play_again = input("ARE YOUR WANT TO PLAY AGAIN ???").lower()
    if(play_again == "no"):
        play=False




