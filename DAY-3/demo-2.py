print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

leftOrRight = input("You're at a cross road. Where do you want to go?\nType \"left\" or \"right\": ")

#! left or right
if leftOrRight == "left" or leftOrRight == "Left" or leftOrRight == "LEFT":
    waitOrSwim = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")

    #! wait or swim
    if waitOrSwim == "wait" or waitOrSwim == "WAIT" or waitOrSwim == "Wait":
        selectDoor = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose: ")

        #! red or yellow or blue
        if selectDoor == "red" or selectDoor == "RED" or selectDoor == "Red":
            print("It's a room full of fire. Game Over.")
        elif selectDoor == "yellow" or selectDoor == "YELLOW" or selectDoor == "Yellow":
            print("You found the treasure! You Win!")
        elif selectDoor == "blue" or selectDoor == "BLUE" or selectDoor == "Blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif waitOrSwim == "swim" or waitOrSwim == "Swim" or waitOrSwim == "SWIM":
        print("You get attacked by an angry trout. Game Over.")

    else:
        print("You chose a door that doesn't exist. Game Over.")

elif leftOrRight == "right" or leftOrRight == "Right" or leftOrRight == "RIGHT":
    print("You fell into a hole. Game Over.")

else:
    print("You chose a door that doesn't exist. Game Over.")