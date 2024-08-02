print("WELOCME TO THE TREASURE ISLAND")
print("YOUR MISSION IS TO FIND A TREASURE")

direction= input('You are at the cross road. Where do you want to go? type "right" or "left.\n').lower()
if direction == "left":
        action= input('You are at the river front. Do you want to "swim" or "wait. \n').lower()
        if action== "wait":
            door_colour=input("Three magical doors appears in front of you with three different colour. Choose 'RED', 'Blue','Yellow'\n").lower()                                     
            if door_colour=="yellow":
                print("You found a treasure and won the game")
            elif door_colour=="red" or door_colour=="blue":
                 print("Game Over")
            else:
                 print("Game Over")
        else:
            print("Game Over") 
else: 
         print("Game Over")
