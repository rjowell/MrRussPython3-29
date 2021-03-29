

def makePasta():
  print("What kind of pasta do you want?")
  pastaChoice = input("A - Cheese Pasta  B - Spaghetti  C - Bowtie Pasta")

  if pastaChoice == "A":
    print("here's your Cheese Pasta")
  elif pastaChoice == "B":
    print("here's your spaghetti")
  elif pastaChoice == "C":
    print("here's your bowtie pasta")
  else:
    print("Sorry We don't have that")

#ORANGE


def makePizza():
  print("Welcome to Shayan's Pizza Palace")
  print("MENU:")
  print("A - Cheese  B - Pepperoni  C - Hawaiian  D - Veggie  E - Meat Loves")

  order = input("What kind of pizza do you want?")

  if order == "A":
    print("Here is your cheese pizza")
  elif order == "B":
    print("Here is your pepperoni pizza")
  elif order == "C":
    print("Here is your Hawiian pizza") 
  elif order == "D":
    print("Here is your Veggie pizza")
  elif order == "E":
    print("Here is your Meaty pizza")
  else:
    print("we don't have that! Try Again")



while True:
  makePizza()
  makePasta()
  


