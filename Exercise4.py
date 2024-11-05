def intro():
 print("You wake up in a dark forest, surrounded by towering trees.")
 print("You have no memory of how you got here.")
 print("You can hear the distant sound of water and the rustle of leaves in the wind.")
 print("What will you do?")
 choice = input("1. Explore the forest\n2. Sit and wait\n> ")
 
 if choice == "1":
    explore_forest()
 elif choice == "2":
    sit_and_wait()
 else:
    print("Invalid choice, try again.")
    intro()

def explore_forest():
 print("\nYou decide to explore the forest. As you walk deeper into the woods,")
 print("you come across a river with a small boat tied to a tree.")
 choice = input("1. Take the boat across the river\n2. Walk along the riverbank\n> ")
 
 if choice == "1":
    cross_river()
 elif choice == "2":
    walk_along_river()
 else:
    print("Invalid choice, try again.")
    explore_forest()

def sit_and_wait():
 print("\nYou sit down and wait for a while. Time passes slowly.")
 print("Suddenly, you hear footsteps approaching from behind.")
 choice = input("1. Turn around to see who it is\n2. Stay still and pretend to be asleep\n> ")
 
 if choice == "1":
    meet_stranger()
 elif choice == "2":
    pretend_sleep()
 else:
    print("Invalid choice, try again.")
    sit_and_wait()

def cross_river():
 print("\nYou untie the boat and begin rowing across the river.")
 print("Halfway across, you see something moving in the water.")
 choice = input("1. Investigate the movement\n2. Row faster to the other side\n> ")
 
 if choice == "1":
    investigate_water()
 elif choice == "2":
    reach_shore()
 else:
    print("Invalid choice, try again.")
    cross_river()

def walk_along_river():
 print("\nYou walk along the riverbank for what feels like hours.")
 print("Eventually, you come across a small wooden cabin.")
 choice = input("1. Knock on the door\n2. Continue walking\n> ")
 
 if choice == "1":
    knock_on_door()
 elif choice == "2":
    continue_walking()
 else:
    print("Invalid choice, try again.")
    walk_along_river()

def meet_stranger():
 print("\nYou turn around and find a tall figure standing behind you.")
 print("The figure introduces themselves as a guide to help you through the forest.")
 print("Will you trust them?")

def pretend_sleep():
 print("\nYou remain still, pretending to be asleep.")
 print("The footsteps get closer, and suddenly you feel a cold hand on your shoulder.")

def investigate_water():
 print("\nYou lean over the side of the boat to investigate the movement.")
 print("Suddenly, a large creature leaps out of the water!")

def reach_shore():
 print("\nYou row faster and safely reach the other side of the river.")
 print("The mysterious movement in the water disappears.")

def knock_on_door():
 print("\nYou knock on the door, but there's no answer.")
 print("The cabin looks abandoned. What will you do next?")

def continue_walking():
 print("\nYou continue walking along the riverbank and find a hidden path leading into the woods.")

if __name__ == "__main__":
 intro()
