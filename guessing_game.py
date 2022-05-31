import random

class GuessingGame():

    def __init__(self,guess):
        self.guess = input()

    def solved(self):
        print(f"Guessing game ")



game = GuessingGame(random.randint(1,100))

last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
