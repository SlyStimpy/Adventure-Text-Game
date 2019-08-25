import random

player_name = input("What is the adventurer's name?")

choice1 = input("What weapon would you like to use. Type in Sword, Axe, or Slingshot. Type in anything else for a random weapon.")

if choice1 == "Sword":
  player_weapon = "Sword"
elif choice1 == "Axe":
  player_weapon = "Axe"
elif choice1 == "Slingshot":
  player_weapon = "Slingshot"
else:
  rand_num = random.randint(1,4)
  if rand_num = 1:
    player_weapon = "Sword"
  elif rand_num = 2:
    player_weapon = "Axe"
  elif rand_num = 3:
    player_weapon = "Slingshot"
  else:
    player_weapon = "Slingshot"
    
print("Congrats " + player_name + ", your weapon is a " + player_weapon + "!")
 
