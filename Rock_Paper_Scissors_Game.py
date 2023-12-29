import random

def DisplayScore(a,b):
    print("Your Score: ",a)
    print("Computer Score: ",b)

UserPoints=0
CompPoints=0
print("hello..")
Options=["R","P","S"]
while True:
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("D. Display Current Scores")
    #print("A. Play Again")
    print("E. Exit")
    Userchoice=input('Enter your choice:')

    CompChoice=random.choice(Options)


    match Userchoice:
        case "R":
            if CompChoice=="S":
                print(" You Won!! ")
                UserPoints+=1
                print("Computer choose ",CompChoice)
            elif CompChoice=="P":
                print("You Lost..")
                CompPoints+=1
                print("Computer choose ",CompChoice)
            else:
                print("It is a Tie") 

        case "P":
            if CompChoice=="R":
                print(" You Won!! ")
                UserPoints+=1
                print("Computer choose ",CompChoice)

            elif CompChoice=="S":
                print("You Lost..")
                CompPoints+=1
                print("Computer choose ",CompChoice)
            else:
                print("It is a Tie") 
        
        case "S":
            if CompChoice=="P":
                print(" You Won!! ")
                UserPoints+=1
                print("Computer choose ",CompChoice)

            elif CompChoice=="R":
                print("You Lost..")
                CompPoints+=1
                print("Computer choose ",CompChoice)
            else:
                print("It is a Tie")

        case "D":
            DisplayScore(UserPoints,CompPoints) 

        case "E":
            print("Exiting the Game")
            break
        case _:
            print("not a valid choice..")
