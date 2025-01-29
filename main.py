import time

# Tama's different states 
state_dictionary = {"Hunger level": 1, "Happiness level": 1, "Energy level": 1, "Health level": 1}

# Hunger review - check and add to hunger state

def hunger_review():
  while True:
    if state_dictionary["Hunger level"] == 3:
     print("I am full!")
     return 
    else:
      hunger_choice = input("Do you want to feed me?")
      if hunger_choice == "Yes":
        state_dictionary["Hunger level"] += 1
        print("Your friend chows down!")
        return
      else:
        print("You have not fed me")

# Happiness function - to check and add to happiness meter

def happiness_review():
  while True:
    if state_dictionary["Happiness level"] == 3:
     print("I am very happy!")
     return 
    else:
      happiness_choice = input("Do you want to play with me?: ")
      if happiness_choice == "Yes":
        state_dictionary["Happiness level"] += 1
        print("Your friend loves playing with you!")
        return
      else:
        print("You have not played with me")

# get user input

def user_input():
  while True:
    user_choice = input("What status would you like to check? Hunger/Happiness/Energy/Health: ")
    if user_choice.lower() == "hunger":
      hunger_review()
      break
    elif user_choice.lower() == "happiness":
      happiness_review()
      break
    else:
      print("No checks done")
      

user_input()
      

  

    
