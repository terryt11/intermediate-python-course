import random
dicerolls = int(input("How many dice would you like to roll? "))
dicesize = int(input("How many sides are the dice? "))

def main():
  dicesum = 0
  for i in range(0,dicerolls):
    roll = random.randint(1, dicesize)
    dicesum += roll
    if roll == 1:
      print(f"You rolled a {roll}, you suck.")
    elif roll==dicesize:
      print(f"You rolled a {roll}... I've seen better.")
    else:
      print(f"You rolled a {roll}")
  print(f'You have rolled a total of {dicesum}')
  
if __name__== "__main__":
  main()