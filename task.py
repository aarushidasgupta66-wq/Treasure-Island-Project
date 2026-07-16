#use 3 single quotes to print multiple lines
print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=(input('You have spawned in a dense forest, the path on which you are standing leads to two directions...\nwhich direction would you like to move?(type: left/right)')).lower()
boat=0
door=0
if direction=="left":
    boat=input("You end up walking for aproximately 15 minutes, then you detect a river bank\n in the distance across the river you see a large gate with a halo surrounding it.\n But you are trying to figure out a way to cross the river.\n By your side you see an enscribed wooden plank which says\n 'Boat Arrives Every 10 Minutes and Commutes to the Other Side of The river'\n you start to decide => \nwould you like to wait for a boat or swim?(type: wait/swim)")
    if boat=="wait":
        door=input('After waiting for 10 minutes, the boat was puntual enough to arrive exactly at the time the wooden plank had mentioned\nYou carefully sit on the creaking bench as the boat automatically sets off,\n the halo of the gate maximises every metre of distance covered\n the other side of the river welcomes a short path that leads to the gate and you willingly step upon it\n The gate automatically opens to three different coloured doors.\n.which door would you like to go in? red, blue or yellow?type:(red/blue/yellow)')
        if door=="red":
            print('You are Burned by fire. game over')
        elif door=="blue":
            print('You are eaten by beasts. game over')
        elif door=="yellow":
            print('The door opens up to a dark atmosphere\n As you grope through insides of the mysteriuos area you discorver a luminiscent Gold chest\n as you begin to reach for it\n The top opens for you and you are awarded an enourmous amount of real gold coins, diamonds, emaralds, sapphires and pearls.\n\n Congratulations you have reached the ultimate treasure of this game!\n you win!')
        else:
            print('game over')
    else:
        print("As you swim, trouts attack you eventually. You die! Game over")
else:
    print("you enter a area closed by bushes. Attacked by a grizzly bear. Game over")
