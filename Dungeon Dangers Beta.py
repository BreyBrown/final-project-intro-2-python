crowbarTool = False #Global variables for Items, these items are used for puzzles in different rooms.
cheeseFood = False
mouseKey = False
wineDrink = False
oldBauble = False

def openingRoom(): #Game starts
    action = ["left", "right", "forward", "down", "give up"]
    print("You awaken to find yourself inside of an empty cell, the cold stone walls reek of mold and decay.")
    print("As you pick yourself up off the ground, brushing your clothes of the dirt and dust until you hear a faint scream.")
    print("You suddenly feel the urge to leave as soon as you possibly can.")

    playerInput = ""
    key = False

    while playerInput not in action: #While loops used to bring player back to input.
        print("available actions: left/right/forward/down")

        playerInput = input()

        if playerInput == "left":
            print("You look to your left and see one of the walls of your cell. Mold is growing in the corner and the wall looks about ready to collapse.")
            print("You could try and tackle it, but common sense says you'd hurt yourself more than you'd hurt the wall.")
        elif playerInput == "right":
            print("You look to your right and see one of the walls of your cell. Blood stains are splattered against the stone, they appear to be dried.")
        elif playerInput == "forward" and key == False:
            print("You walk up to the door of your cell. Peering through the small window of the wooden door, you can barely make out the cellblock.")
            print("It's not worth trying to break it down, the wood seems sturdy, and your body feels too weak to try.")
        elif playerInput == "forward" and key == True:
            print("You walk up to the door and put the key inside the lock, turning it, it unlocks with a click. You creak the door open and step outside the room.")
            cellBlock()
        elif playerInput == "down" and key == False:
            print("You look down at the ground, noticing a glimmer at your feet, you reach down and pick it up. It's a conviently placed key, lucky you!")
            key == True
        elif playerInput == "down" and key == True:
            print("You look down again, hoping to maybe find a scrap of food. Don't let the luck go to your head, pal.")

        elif playerInput == "give up":
            print("You allow your hopelessness to take over, collapsing to the ground and fainting from the stress.")
            print("You will never escape and you've chosen to accept your fate.")
            quit()

        else:
            print("You'll need to try something else.")

def cellRoom():
    action = ["left","right","back","look"]
    print("You enter the cell, it's litered with boxes and barrels. The room has a very... unique scent.")

    playerInput = ""

    while playerInput not in action:
        print("left/right/back/look")
        playerInput = input()

        if playerInput == "left":
            print("You check the barrels to your right. The scent doesn't seem to be coming from here but you can't help but feel a little curious as to what's inside.")
        elif playerInput == "left" and crowbarTool == True:
            print("Using the crowbar you try to pry open the barrel, it doesn't seem to work. You smack the barrel with the crowbar in defiance.")
            print("Some quality wine pops out of the barrel top in a bottle. You aren't sure how that works, but you're going to carry on anyway.")
            wineDrink == True

        if playerInput == "right":
            print("You check the boxes to your right, they emit a stinky odor. The scent is... familiar to you, the scent of food maybe?")
        elif playerInput == "right" and crowbarTool == True:
            print("Using the crowbar you pry open smelly box, and after a bit of effort the top pops off. /n Looking inside you find a lot of cheese.")
            print("Maybe this will come in handy, or maybe it'll be good to at least have something for a last meal.")
            cheeseFood == True

        if playerInput == "look":
            print("You look admist the boxes and barrels. Hm? Seems there's a crowbar here, might be useful for later. /n You take the Crowbar.")
            crowbarTool == True

        elif playerInput == "back":
            cellBlock
            
        else:
            print("Maybe there are some useful things within this room?")

def cellBlock():
    action = ["left", "right", "forward", "back" "smell"]
    print("You enter the cell block. The sound of water droplets dripping against the musty stone floor echo through the area.")
    print("In front of you is another cell, the door appears to have been smashed open.")

    playerInput = ""

    while playerInput not in action:
        print("left/right/forward/back/smell.")
        playerInput = input()

    if playerInput == "left":
         cellBlock_2()

    elif playerInput == "right":
            print("You look to your right and see that it's merely a dead-end, a rat scurries past your vision and into a nearby cell.")

    elif playerInput == "forward":
            cellRoom()

    elif playerInput == "back":
            print("There's nothing for you in your cell block, unless you feel like eating some mold.")

    elif playerInput == "smell":
            print("You decide to take in a deep whiff of the air. Ahh, nothing like the scent of mold and rot to fuel your desire for fresh air.")

def cellBlock_2():
    action = ["left", "right", "forward", "back", "inspect"]
    print("You continue down the hall of the cell block. The air reeks of rotting corpses, and the doors to the remaining cells are smashed apart.")
    playerInput = input()

    while playerInput not in action:
        print("Doesn't look like you can go that way.")

        if playerInput == "left":
            print("You look to the cell room on your left, the pungent scent makes causes you to cringe. You back away from the cell.")

        if playerInput == "right":
            print("You look to the cell room on your right, the scent isn't nearly as bad as the rest of the place.")
            print("The ground is covered in blood, seems pretty recent. You hope that whatever caused it doesn't come back.")
        
        elif playerInput == "forward":
            trapRoom_1()

        elif playerInput == "back":
            cellBlock()
        
        elif playerInput == "inspect":
            print("You choose to inspect the ground around you, but find nothing of value.")
    
def trapRoom_1():
    action = ["forward", "back", "platforms", "hint"]
    print("Before you lay a bed of spikes, and across the way you can see a glimmer admist a bundle of barrels and boxes.")
    print("Around you are more boxes and barrels, oddly enough.")
    playerInput = ""

    platform = False

    while playerInput not in action:
        print("forward/back/platforms/hint")

        if playerInput == "forward" and platform == False:
            print("There is no way forward, perhaps you could make one?")
        else:
            print("You carefully traverse the makeshift platforms you have created, and reach the other side. /n You open the unlocked door.")
            studyRoom()

        if playerInput == "back":
            cellBlock()

        elif playerInput == "platforms":
            print("You decide to make platforms out of the various boxes and barrels.")
            print("Though it seems risky, the boxes seem durable enough to withstand your weight.")
            platform == True

        elif playerInput == "hint":
            print("Try using your surroundings to your advantage, there must be a way to cross without impaling yourself.")

def studyRoom():
    action = ["talk", "trade", "back", "mouse"]
    print("As you enter the room a tired looking man in a rocking chair greets you casually, though with little interest in you as you hear a tiny mouse squeak in the corner.")

    playerInput = ""

    while playerInput not in action:
        print("talk/trade/back/mouse")

        if playerInput == "talk":
            print("You approach the old man, and try to get his attention. /n He responds 'We don't get many vistors in these parts.'")
            print("You ask him where you are, he responds 'Well, you're currently in my study.' /n Well that's not the answer you were hoping for.")
        elif playerInput =="trade" and wineDrink == False:
            print("You approach the old man with the intent of doing buisness. Unfortunatly you don't have anything he wants and he goes back to rocking in his chair.")
        elif playerInput =="trade" and wineDrink == True:
            print("You approach the old man with the bottle of wine and offer it to him in exchange for something of equal value.")
            print("The old man looks up at the wine, he grasps at it and pulls it out of your hands, popping the cork and taking a swig.")
            print('After his swig he feels the kick of the potent beverage. Turning back to you he says, "Thanks youngin. You can have this lil trinket"')
            oldBauble = True
            wineDrink = False

        elif playerInput == "back":
            trapRoom_1()
        elif playerInput == "mouse" and cheeseFood == False:
            print("You approach the mouse. It looks up at you from the book it was reading.")
            print('"H-hello.." the mouse shyly squeaks.')
            print("You're curious as to why it can talk. But it only replies with 'The old man told me how.'")
            print("You decide to not question it further and go back to what you were doing")
        elif playerInput == "mouse" and cheeseFood == True:
            print("As you approach the mouse it's nose starts to twitch. It can smell the cheese you have on you.")
            print("'Hello!! Uhm.. are you going to eat that cheese you have?' It asks you excitedly.")
            print("Relcutantly you part ways with the food you had found and give it to the mouse, and in return it hands you a key. It nibbles on the cheese and you walk away.")
            mouseKey = True
            cheeseFood = False
        
def main():
    print("Welcome to the dungeons.")
    print("I will be your guide through this mini-adventure.")
    print("Be warned that this dungeon is incredibly dangerous, you will find tricks and traps aplenty.")
    print("This mini-adventure is not for the faint of heart...")

    openingRoom()

main()