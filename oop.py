########### INITIATION ###########

class Dog():
  # Class object attribute
  species = 'Pup'
  skill = 'Eating'

  # Initiation (self, arg1, ..., argN)
  def __init__(self, breed, name): 
    self.breed = breed
    self.name = name


# dog1 = Dog(breed = 'Corgi', name = 'Coco')
# print(dog1.name, 'the', dog1.breed) 



############ CLASS METHODS ############

class Circle():
  pi = 3.14

  def __init__(self, radius=1):
    self.radius = radius

  def area(self):
    print(self.radius**2 * Circle.pi)

  # mycircle.radius = n
  def set_radius(self, r):
    self.radius = r

# mycircle = Circle(3)
# print(mycircle.radius)
# mycircle.set_radius(100)
# mycircle.area()



############ INHERITANCE ###############

class Animal():
  
  def __init__(self):
    print('ANIMAL CREATED')

  def who_am_i(self):
    print('I AM ANIMAL')
  
  def eat(self):
    print('YUMMM')

# mya = Animal()
# mya.who_am_i()
# mya.eat()

class Dolphin(Animal):

  def __init__(self):
    # Animal.__init__(self) # not necessary but ensures initiation beyond just inheritence 
    print("DOLPHIN CREATED")

  def speak(self): 
    print("HELLO HUMANS")

  def eat(self):
    print("THIS IS DELICIOUS!")


# mya = Dolphin()
# mya.who_am_i()
# mya.eat()



############ INHERITANCE ###############

class Book():
  
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  # print(b) will return string representation of the instance with all its attributes
  def __str__(self):
    return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)

  # len() method
  def __len__(self):
    return self.pages
  
  # def __del__(self):
  #   print('NOOOO! GOODBYE.')
  
  def test(self):
    print(self.title)
  
b = Book('Python', 'Quang', 200)
print(b)
del b