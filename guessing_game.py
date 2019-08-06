import random

def Game():
  '''
  A simple guessing game where players have to guess and input a 3-digit integer
  into the prompt
  '''
  digits = list(range(10))
  random.shuffle(digits)
  solution = digits[:3]
  print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
  print("Code has been generated, please gues a 3 digit number")
  promptInput(solution)

def match(g, a):
  '''
  A 'Match' in the game is when user has at least one number guessed correctly
  and on the right place value (ones, tens, or hundreds place)
  '''
  for i in range(len(g)):
    if g[i] == a[i]:
      return True
  return False

def close(g, a):
  '''
  A 'Close' in the game is when user has at least one number guessed correctly
  but it/they might not be on the correct place value
  '''
  for num in g:
    if num in a:
      return True
  return False

def promptInput(answer):
  '''
  Recurscive logic of the game, keep prompting until correct
  '''
  guess = [int(item) for item in list(input("What is your guess? ")[:3])]
  if guess == answer:
    user_feedback = input("~~~~YOU WIN!!!~~~~ Play again? [y/n]")
    if user_feedback[0] == 'y':
      return Game()
    else:
      print("Thanks for playing. Goodbye!")
  elif match(guess, answer):
    print('Match!')
    return promptInput(answer)
  elif close(guess, answer):
    print('Close!')
    return promptInput(answer)
  else:
    print('Nope!')
    return promptInput(answer)

Game()
