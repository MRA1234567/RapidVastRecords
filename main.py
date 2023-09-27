import random

Pchoice = input("Rock, Paper or Scissors: ")
Achoice = random.randint(1, 3)

if Pchoice == "Rock":
  if Achoice == 1:
    print("Draw")
  elif Achoice == 2:
    print("You lose")
  else:
    print("You win")

if Pchoice == "Paper":
  if Achoice == 1:
    print("You win")
  elif Achoice == 2:
    print("Draw")
  else:
    print("You lose")

if Pchoice == "Scissors":
  if Achoice == 1:
    print("You lose")
  elif Achoice == 2:
    print("You win")
  else:
    print("Draw")
