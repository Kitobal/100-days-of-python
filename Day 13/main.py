############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1,21): # the start is inclusive, but the end is exclusive
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # lists start at 0 so index 6 does not exist
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: #1994 was not included before
  print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?")) #the input was not converted to int
if age > 18:
    print(f"You can drive at age {age}.") #had wrong indentation and was not an f-string

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #was comparing instead of assigning (== instead of =)
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #this line was outside the for loop , co only the last new_item was added
  print(b_list)

mutate([1,2,3,5,8,13])