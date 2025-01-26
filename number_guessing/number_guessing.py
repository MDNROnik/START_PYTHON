import random

keep_going = True
lower_bound = 0
while keep_going:
    lower_bound = input("What is the Lower Bound of the range ?")
    if lower_bound.isdigit():
        keep_going = False
        lower_bound = int(lower_bound)
    else:
        print("Please Enter A Number")

keep_going = True
upper_bound = 0
while keep_going:
    upper_bound = input("What is the Upper Bound of the range ?")
    if upper_bound.isdigit():
        keep_going = False
        upper_bound = int(upper_bound)
    else:
        print("Please Enter A Number")

# print(lower_bound,upper_bound)

random_number = random.randint(lower_bound, upper_bound)

keep_going = True
score = 0
while (keep_going):
    rand = input("Guess The Number !!! ")
    if (rand.isdigit()):
        rand = int(rand)
    else:
        print("Please Enter A Number !!! ")
        continue
    print(rand, random_number)
    if (rand == random_number):
        print("Congratulations Now You Guess The Number With Score OF ", score)
        break
    elif (rand > random_number):
        print("Your Guess Number is Larger Then Generated Number ")
        score = score + 1
    else:
        print("Your Guess Number is Smaller Then Generated Number ")
        score = score + 1

print("Want to play again then run the python file again >>>")
