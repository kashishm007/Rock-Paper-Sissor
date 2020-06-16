import random


outputs = ["Rock", "Paper", "Sissor"]
c_score = 0
p_score = 0
ch = "y"
while ch == "y":
    computer = outputs[random.randint(0,2)]
    player = input("Choose: ")
    if player != "Rock" and player != "Paper" and player != "Sissor" :
        player = input("Choose again: ")
    elif player == computer:
        print("tie", computer)
        c_score+=1
        p_score+=1
    elif player == "Rock" and computer == "Paper":
        print("you loose",computer)
        c_score+=1
    elif player == "Rock" and computer == "Sissor":
        print("you win",computer)
        p_score+=1
    elif player == "Paper" and computer == "Sissors":
        print("you lose",computer)
        c_score+=1
    elif player == "Paper" and computer == "Rock":
        print("you win",computer)
        p_score+=1
    elif player == "Sissor" and computer == "Rock":
        print("you lose",computer)
        c_score+=1
    elif player == "Sissor" and computer == "Paper":
        print("you win",computer)
        p_score+=1
    ch = input("Play again (y/n)")
print("Your Score: ", p_score, " Computer Score: ", c_score)

