import random

def Game():
  '''
  A simple guessing game where players have to guess and input a 3-digit 
  integer into the prompt with following rules:

    - A 'Match' feedback is when user has at least one number guessed 
      correctly and on the right place value (ones, tens, or hundreds
      place)
    - A 'Close' feedback is when user has at least one number guessed
      correctly but it/they might not be on the correct place value
    - A 'Nope' feedback is when user has no matches 
  '''
  print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
  print("Code has been generated, please guess a 3 digit number")
  solution = generate_solution()
  run_game_prompt(solution)


def generate_solution():
  '''
  Generates a random 3-digit number to be used as a solution to the game
  '''
  digits = list(range(10))
  random.shuffle(digits)
  return digits[:3]

def match(g, a):
  '''
  Checks a 'Match' game condition
  '''
  for i in range(len(g)):
    if g[i] == a[i]:
      return True
  return False

def close(g, a):
  '''
  Checks a 'Close' game condition
  '''
  for num in g:
    if num in a:
      return True
  return False

def run_game_prompt(answer):
  '''
  Recurscive logic of the game, keep prompting until correct
  '''
  guess = [int(item) for item in list(input("What is your guess? ")[:3])]
  if guess == answer:
    user_feedback = input("~~~~YOU WIN!!!~~~~ Play again? [y/n]:")
    if user_feedback[0] == 'y':
      run_game_prompt(generate_solution())
    else:
      return print("Thanks for playing. Goodbye!")
  elif match(guess, answer):
    print('Match!')
    return run_game_prompt(answer)
  elif close(guess, answer):
    print('Close!')
    return run_game_prompt(answer)
  else:
    print('Nope!')
    return run_game_prompt(answer)

Game()
