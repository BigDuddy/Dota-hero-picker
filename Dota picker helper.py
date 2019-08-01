from Useful_tools import Hero
from Useful_tools import Lane_counter

# dota picker helper project

# enter hero data
# -> store lane + role inside a variable of Hero class

# Global variables
shadow_shaman = Hero("Support" + "Pusher" + "Ranged", "Sidelane" + "Midlane")
juggernaut = Hero("Carry" + "Melee", "Safelane")
magnus = Hero("Initiator" + "AOE" + "Melee", "Sidelane" + "Midlane")
invoker = Hero("Nuker" + "Disabler" + "Ranged" + "AOE", "Midlane")
dark_seer = Hero("Initiator" + "Melee" + "AOE", "Offlane")

sidelane_counter = Lane_counter("Side", 0)
midlane_counter = Lane_counter("Mid", 0)
offlane_counter = Lane_counter("Off", 0)
safelane_counter = Lane_counter("Safe", 0)

heroes_picked = 0

# show heroes----- TO DO

# be able to click heroes----- TO DO

# storing picked hero----- TO DO

# Checking hero data and updating variables for the algorithm to use

def check_data(clicked_hero):
    if "Sidelane" in clicked_hero:
        sidelane_counter += 1
    if "Midlane" in clicked_hero:
        midlane_counter += 1
    if "Offlane" in clicked_hero:
        offlane_counter += 1
    if "Safelane" in clicked_hero:
        safelane_counter += 1


# apply results to display----- TO DO

# do it again (prob while loop using heroes_picked)
