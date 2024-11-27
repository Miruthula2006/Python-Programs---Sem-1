import random
while True:
  print("DICE ROLLING")
  print("1.roll\n2.exit")
  user_input=input()
  if user_input=="roll":
        dice=random.randrange(1,7)
        print(f"You rolled a {dice}")
  elif user_input=="exit":
        print("Thanks for Playing")
        quit()
  else:
        print("ENTER VALID INPUT")


import random
restaurants = [
    "Saravana Bhavan",
    "Anjappar Chettinad",
    "Sangeetha",
    "Dosa Plaza",
    "Madras Pavilion",
    "Kumarakom Restaurant",
    "Buhari Hotel"
]
while True:
  print("Pick a restaurant")
  print("1.pick\n2.bye")
  user_input=input()
  if user_input=="pick":
    picked=random.choice(restaurants)
    print(f"You Picked the restaurant {picked}")
  elif user_input=="bye":
    print("Goodbye")
    quit()
  else:
        print("ENTER VALID INPUT")
  
    
def validate(username):
  if not username[0].isalpha():
    return "Must start with a letter"
  if not username.replace("_","").isalnum():
    return "Must contain only letters, numbers, or underscores"
  if not (5 <= len(username) <= 15):
    return "Must be between 5 and 15 characters"

  return "valid"
def validity():
  username=input()
  result=validate(username)
  if result=="valid":
    print("Username is valid")
  else:
    print(f"Username is not valid , {result}")
validity()
  
















