import time
import random

#define a function, if hunger less than 8 (for example) OR energy is less than 3. Then if random.random < 0.3 then sick == true.

def random_ill():
  if state_dictionary["Health level"] < 2 or state_dictionary["Energy level"] < 2:
    if random.random() <0.3:
      state_dictionary["Health level"] = True
      print("Oh no, your friend isn't well!")

def cure_tama():
  if state_dictionary["Health level"]:
    state_dictionary["Health level"] = True
    print("You gave your friend medication!")
    state_dictionary["Health level"] = False
  else:
    print("Your friend is well")  

# Tama's different states 
state_dictionary = {"Hunger level": 5, "Happiness level": 5, "Energy level": 5, "Health level": False}

# Hunger review - check and add to hunger state

def hunger_review():
  if state_dictionary["Hunger level"] == 10:
    print("I am full!")
    return 
  else:
    hunger_choice = input("Do you want to feed me? ")
    if hunger_choice == "Yes":
      state_dictionary["Hunger level"] += 3
      print("Your friend chows down!")
      return
    else:
      print("You have not fed me")
    random_ill()

# Happiness function - to check and add to happiness meter

def happiness_review():
  if state_dictionary["Happiness level"] == 10:
    print("I am very happy!")
    return 
  else:
    happiness_choice = input("Do you want to play with me?: ")
    if happiness_choice == "Yes":
      state_dictionary["Happiness level"] += 4
      print("Your friend loves playing with you!")
      return
    else:
      print("You have not played with me")
    random_ill()


def energy_review():
  if state_dictionary["Energy level"] == 10:
    print("I am very rested!")
    return 
  else:
    energy_choice = input("Put your friend to bed?: ")
    if energy_choice == "Yes":
      state_dictionary["Energy level"] += 3
      print("Your friend is in bed")
      return
    else:
      print("I am tired!")
    random_ill()

# get user input

def gameplay():
  while True:
    user_choice = input("What would you like to do? Feed/Play/Rest/Display Stats: ")
    if user_choice.lower() == "feed":
      hunger_review()
    elif user_choice.lower() == "play":
      happiness_review()
    elif user_choice.lower() == "rest":
      energy_review()
    elif user_choice.lower() == "display stats":
      print(f"Your friend stats are: {state_dictionary}")
    else:
      print("No checks done")

    tick()
    time.sleep(5)
      
# Stats initial state. User turns on, selects pet action, state 2. finishes. All stats decrease.  Tick.

def tick(): #simulate time passing and the impact on stats
  state_dictionary['Hunger level'] = max(0, state_dictionary['Hunger level'] - 2)
  state_dictionary['Happiness level'] = max(0, state_dictionary['Happiness level'] - 3)
  state_dictionary['Energy level'] = max(0, state_dictionary['Energy level'] - 1)
  

gameplay()

      

  

    
