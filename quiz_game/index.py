#game start with question and give options
def new_game():
    guesses = []
    correct_guesses = []
    que_num=0
    for key in questions:
        print(key)
        print(options[que_num])
        que_num=que_num+1
        guesses.append( input("Ans The Ques - ").upper()  )
        correct_guesses.append( questions.get(key) )
        
        


    # print(guesses)

    check_ans(guesses,correct_guesses)



def check_ans(guesses,correct_guesses):
    i = 1
    score = 0

    for key in questions:
        print(i," que ans is ",correct_guesses[i-1]," and your given ans is ",guesses[i-1],end=" --- ")
        if(correct_guesses[i-1] == guesses[i-1]):
            print(" Your ans is corrent")
            score=score+1
        else:
            print("Sorry your ans is wrong")
        i=i+1
    
    display_scores(score)
    




def display_scores(score):
    print("Your Score Is ",score)
    play_again()
    
def play_again():
    do_play_again = input("Do you want to play again ? ").lower()
    if(do_play_again=="yes"):
        new_game()
    else:
        print("See You AGAIN !!!")

questions = {
    "Who invented python ?" : "A",
    "Which year python invented ?" : "B",
    "Python is tributed to which comedy group ?" : "C",
    "Is the Earth round ?" : "A",
}

options = [
    ["A. Guido van Rossum" , "B. Elon Mush", "C. Bill Gates", "D. Mark Zuckerbury"],
    ["A. 1989" , "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island" , "B. Smosh", "C. Monty Python", "SNL"],
    ["A. True" , "B. False", "C. Somethimes", "D. Is Earth Is Real"]
]


new_game()