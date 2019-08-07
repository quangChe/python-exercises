NAMES = [
  'quang',
  'nicole',
  'nica',
  'brian',
  'michael',
  'robert',
]

if __name__ == '__main__':
  print('Funk script')

def can_u_take_me_to_func_e_town():
  name = input('Hello, what is your name? ')
  if name.lower() in NAMES:
    return proceed_to_func()
  else:
    print('Sorry, you\'re not ready to funk. Train harder.')

def proceed_to_func():
  print("Getting funky...")
  print("FUNKAAYYY!")
  again = input('Wanna go again? ')
  if again[0].lower() == 'y':
    return proceed_to_func()
  else:
    pass
