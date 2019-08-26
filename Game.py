import random

player_name = input("What is the adventurer's name?")

print("Sword: Medium powered weapon. Can only attack from 1 space away. Has a 95% hitrate.")
print("Axe: Most powerful weapon. Can attack from 2 spaces away. However, only has a 85% hitrate.")
print("Slingshot: Weakest weapon of the 3. Can attack from 4 spaces away. Has 90% hitrate")
print("")

choice1 = input(
    "What weapon would you like to use. Type in Sword, Axe, or Slingshot. Type in anything else for a random weapon.")
print("")


if choice1 == "Sword":
    player_weapon = "Sword"
elif choice1 == "Axe":
    player_weapon = "Axe"
elif choice1 == "Slingshot":
    player_weapon = "Slingshot"
else:
    rand_num = random.randint(1, 4)
    if rand_num == 1:
        player_weapon = "Sword"
    elif rand_num == 2:
        player_weapon = "Axe"
    elif rand_num == 3:
        player_weapon = "Slingshot"
    else:
        player_weapon = "Slingshot"

print("Congrats " + player_name + ", your weapon is a " + player_weapon + "!")
print("")

field_size = random.randint(5, 11)
print("The field size is " + str(field_size) + "x" + str(field_size))

field = []
for i in range(field_size):
    field.append([])
    for j in range(field_size):
        field[i].append(random.randint(0,11))
        #Numbers 0-7 mean nothing appear. 8 is a healing space. 9 is an enemy. 10 is a trap

not_valid_start = []
start = [random.randint(0,field_size), random.randint(0,field_size)]
field[start[0]][start[1]] = -1

print(field)
print(start)
game_playing = True

print("At any time type Q to stop playing")

# Gameplay:
# For start, enemies are stationary. You are allowed to see 3 spaces in front of you in all 4 cardinal directions
# Once you kill an enemy their space on the board becomes harmless.
# Traps instantly end the game if you stand on one. You cannot see traps, however a message will pop up saying you have x amount of traps around you that you can detect within the 3 spaces
# If you are one space away from an enemy they can attack you
# For now (this will be changed later), enemies only take one hit to kill

#Every turn, you can go North, East, South, or West

player_HP = 100

position = start
temp_pos = position
trap_count = 0
north_enemy_count = 0
south_enemy_count = 0
west_enemy_count = 0
east_enemy_count = 0

while game_playing:
    #Tracking north enemies
    for k in range(3):
        if temp_pos[1] == 0:
            break
        else:
            if field[temp_pos[0]][temp_pos[1]] == 10:
                trap_count +=1
            elif field[temp_pos[0]][temp_pos[1]] == 9:
                north_enemy_count +=1
            temp_pos[1] = temp_pos[1]- 1
    
    player_intent = input("Howdy")
    if player_intent == "Q":
        game_playing = False
        break
