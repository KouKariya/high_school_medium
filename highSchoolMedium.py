# High School Medium
# Written in Python3. 
# Game pits player against spirit in a retro style turn based RPG battle 
# Written by Jesse Gallarzo
# coding=utf-8

## TODO ##
# Fix main loop to track when Player wins(not just when Monster wins)
# Optimize RUN option
# Make ITEMS usable
# Move player and monster stats to objects
# Start looking at GUI for game(pygame)
# Create map Object to track location

#Character Variables
# / HP/ ATT/ SPD/
monster_stats = [7,3,3]

# / HP/ ATT/ SPD/ LCK/
player_stats = [7,2,4,1]


#Game Variables
monster_wins = False
player_escapes = False

#Function that deals with assigning turns and dealing combat damage. Returns boolean variables that break the main method.
#TODO turn While() loop into main function.
def battle(sur_hp,kil_hp,sur_attack,kil_attack,sur_speed,kil_speed):
    global player_escapes
    global monster_wins
    #If the player is faster, damage the monster first
    if(sur_speed > kil_speed):
        monster_stats[0] = monster_stats[0] - sur_attack
        print("The monster takes " + str(sur_attack) + " damage!")
        #Win-Condition
        if monster_stats[0] <= 0:
            print("You managed to fend off the attacker and survived!")
            player_escapes = True
            monster_wins = False #Will only run if both instances are declared here; Look into further ; change other win cons
            return
        player_stats[0] = player_stats[0] - kil_attack
        print("You take " + str(kil_attack) + " damage!")
        #Win-Condition
        if player_stats[0] <= 0:    
            print("The monster got to you. Game over...")
            monster_wins = True
            player_escapes = False #Will only run if both instances are declared here; Look into further ; change other win cons
            return
    #If the monster is faster, damage the player first.
    #TODO fix 'else' statement to be better defined. I.e. 2nd if statement or look into elif again
    else:
        player_stats[0] = player_stats[0] - kil_attack
        print("You take " + str(kil_attack) + " damage!")
        #Win-Condition
        if player_stats[0] <= 0:
            print("The monster got to you. Game over...")
            monster_wins = True
            player_escapes = False
            return
        monster_stats[0] = monster_stats[0] - sur_attack
        print("The monster takes " + str(sur_attack) + " damage!")
        #Win-Condition
        if monster_stats[0] <= 0:
            print("You managed to fend off the evil spirit and survived!")
            player_escapes = True
            monster_wins = False
            return
        
#Game Start
print("A malevolent spirit blocks your way!")
while(player_escapes is False and monster_wins is False):

    #Playable actions for the Player
    print("What will you do?")
    print("**********")
    print("FIGHT")
    print("Use ITEM")
    print("RUN")
    print("**********")
    action = input()
    #action = input("What do you do? FIGHT? or RUN? ")

    #Escape from attack.
    if action.upper() == "RUN":
        player_escapes = True
        print("You got away safely!")

    #Fight the monster.
    elif action.upper() == "FIGHT":
        battle(player_stats[0], monster_stats[0], player_stats[1], monster_stats[1], player_stats[2],monster_stats[2])
        print("")
        print("player's health: " + str(player_stats[0]))
        print("monster's health: " + str(monster_stats[0]))
        print("")
        
    #Invalidates any other input except for desired commands.
    else:
        print("Invalid option! Try again.")

    #If none of the game states resolve, restart
