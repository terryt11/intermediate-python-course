import random
dicerolls = 2

def main():
  dicesum = 0
  for i in range(0,dicerolls):
    roll = random.randint(1, 6)
    dicesum += roll
    print(f"You rolled a {roll}")
  print(f'You have rolled a total of {dicesum}')
  
if __name__== "__main__":
  main()