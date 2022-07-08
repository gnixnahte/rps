import random
comp = ["rock", "paper", "scissors"]
cc = random.choice(comp)

n = input("Choose between rock paper and scissors: ")
print("I, the computer, choose",cc)

if cc == n:
    print("The match is a tie! ")
elif cc == ("rock"):
    if n == ("paper"):
        print("You win!")
    elif n == ("scissors"):
        print("You lose!")
      
elif cc == ("paper"):
    if n == ("rock"):
        print("You Lose!")
    elif n == ("scissors"):
        print("You Win!")
elif cc == ("scissors"):
    if n == ("paper"):
        print("You lose!")
    elif n == ("rock"):
        print("You win!")