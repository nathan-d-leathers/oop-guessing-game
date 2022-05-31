import random

class GuessingGame:

    def __init__(self, num, boolean=False):
        self.num = num
        self.boolean = boolean
  
    def guess(self,number):
      input_guess = int(number)

      if input_guess == self.num:
        self.boolean = True
        return "correct"
      elif input_guess > self.num:
        return "high"
      elif input_guess < self.num:
        return "low"

    def solved(self):
        return(self.boolean)

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
