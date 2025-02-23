"""This is a small project of my own take on a game of Rock, Paper, Scissors"""

import random

while True:
    player_action = input("\nEnter your animal of choice: bee, bun, corvid, cat, wolf, human\n")
    # when we put css in, I would like to add pictures of the animals of choice that the player can choose from. Maybe even randomize the photo shown each playthrough.
    possible_actions = ["bee", "bun", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)

    # make sure there aren't any lazy duplicates with potential dialogues. I want wolf vs cat to have a different scenario than cat vs wolf, even if the winner is the same.
    # I like this as a dialogue potential: ... sensitive ears pick up the cautionary buzz of the bee and is terrified into running back home. You win!

    print(f"\nIt's {player_action} vs {computer_action}.\n")

    def element_battle(water_vs_fire,
                   water_vs_earth,
                   water_vs_air_win,
                   water_vs_air_lose,
                   fire_vs_water,
                   fire_vs_earth,
                   fire_vs_air_win,
                   fire_vs_air_lose,
                   earth_vs_water,
                   earth_vs_fire,
                   earth_vs_air_win,
                   earth_vs_air_lose,
                   air_vs_water_win,
                   air_vs_water_lose,
                   air_vs_fire_win,
                   air_vs_fire_lose,
                   air_vs_earth_win,
                   air_vs_earth_lose
                   ):
        print("It's a tie! Looks like being basic animals isn't enough for you two. It's time to adopt a... 'special' quality to apply to your animal of choice.\n")
        
        player_action_element = input("Choose a basic element: water, fire, earth, or air\n")
        possible_element_actions = ["water", "fire", "earth", "air"]
        computer_action_element = random.choice(possible_element_actions)

    
        
        print(f"\nIt's {player_action_element} {player_action} vs {computer_action_element} {computer_action}.")

        #do we want an animal + element = something like "fire bee" or animal + element = something like "wasp"?
        #how will we change a bee + fire into a wasp in the dialogue?
        #be aware that this change will probably need to be made outside of this function

        if player_action_element == computer_action_element:
            print("Another tie?? Jeez, well then, I suppose both of you win... for now. >_>") #go in depth again
        if player_action_element == "water":
            if computer_action_element == "fire":
                print(water_vs_fire) #needs dialogue that will be fleshed out above in the parameters of the function
            elif computer_action_element == "earth":
                print(water_vs_earth) #needs dialogue
            else:
                waterair_win_or_lose_actions = [water_vs_air_win, water_vs_air_lose] #needs dialogue
                computer_action_water_vs_air = random.choice(waterair_win_or_lose_actions)
                print(computer_action_water_vs_air)
        elif player_action_element == "fire":
            if computer_action_element == "water":
                print(fire_vs_water) #needs dialogue
            elif computer_action_element == "earth":
                print(fire_vs_earth) #needs dialogue
            else:
                fireair_win_or_lose_actions = [fire_vs_air_win, fire_vs_air_lose] #needs dialogue
                computer_action_fire_vs_air = random.choice(fireair_win_or_lose_actions)
                print(computer_action_fire_vs_air)
        elif player_action_element == "earth":
            if computer_action_element == "water":
                print(earth_vs_water) #needs dialogue
            elif computer_action_element == "fire":
                print(earth_vs_fire) #needs dialogue
            else:
                earthair_win_or_lose_actions = [earth_vs_air_win, earth_vs_air_lose] #needs dialogue
                computer_action_earth_vs_air = random.choice(earthair_win_or_lose_actions)
                print(computer_action_earth_vs_air)
        else:
            if computer_action_element == "water":
                water_win_or_lose_actions = [air_vs_water_win, air_vs_water_lose] #needs dialogue
                computer_action_air_vs_water = random.choice(water_win_or_lose_actions)
                print(computer_action_air_vs_water)
            elif computer_action_element == "fire":
                fire_win_or_lose_actions = [air_vs_fire_win, air_vs_fire_lose] #needs dialogue
                computer_action_air_vs_fire = random.choice(fire_win_or_lose_actions)
                print(computer_action_air_vs_fire)
            else:
                earth_win_or_lose_actions = [air_vs_earth_win, air_vs_earth_lose] #needs dialogue
                computer_action_air_vs_earth = random.choice(earth_win_or_lose_actions)
                print(computer_action_air_vs_earth)

    if player_action == "bee":
        if computer_action == "bee":
            element_battle("water bee beats fire bee",
                       "water bee loses to ground bee",
                       "water bee beats air bee",
                       "water bee loses to air  bee",
                       "fire bee loses to water bee",
                       "fire bee beats earth bee",
                       "fire bee beats air bee",
                       "fire bee loses to air bee",
                       "earth bee beats water bee",
                       "earth bee loses to fire bee",
                       "earth bee beats air bee",
                       "earth bee loses to air bee",
                       "air bee beats water bee",
                       "air bee loses to water bee",
                       "air bee beats fire bee",
                       "air bee loses to fire bee",
                       "air bee beats earth bee",
                       "air bee loses to earth bee")
        elif computer_action == "bun":
            print("In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n")
        elif computer_action == "corvid":
            print("Corvid eats the bee. You lose!\n")
        elif computer_action == "cat":
            print("Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n")
        elif computer_action == "wolf":
            print("The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n")
        else:
            humanandbee_win_or_lose_actions = ["Human is allergic to the bee and is hospitalized. You win!\n", "Human smacks the bee with a newspaper, crushing it immediately. You lose!\n"]
            computer_action_bee_vs_human = random.choice(humanandbee_win_or_lose_actions)
            print(computer_action_bee_vs_human)
    elif player_action == "bun":
        if computer_action == "bee":
            print("Despite inhabiting the same garden, the bun's ability to sneak allows it to be overlooked while the human notices the constant buzzing of the bee's hive and has the colony removed. This allows the bun a distraction that leads to the success of its family. You win!\n")
        elif computer_action == "bun":
            element_battle("water bun beats fire bun",
                       "water bun loses to ground bun",
                       "water bun beats air bun",
                       "water bun loses to air  bun",
                       "fire bun loses to water bun",
                       "fire bun beats earth bun",
                       "fire bun beats air bun",
                       "fire bun loses to air bun",
                       "earth bun beats water bun",
                       "earth bun loses to fire bun",
                       "earth bun beats air bun",
                       "earth bun loses to air bun",
                       "air bun beats water bun",
                       "air bun loses to water bun",
                       "air bun beats fire bun",
                       "air bun loses to fire bun",
                       "air bun beats earth bun",
                       "air bun loses to earth bun")
        elif computer_action == "corvid":
            print("The corvid sees the bun outside of their den and alerts its presence to nearby wolves. The bun is hunted and both enjoy the meal. You lose!\n")
        elif computer_action == "cat":
            print("The cat, brought in as pest control, drives the bun and its family from the garden it lived in from birth. You lose!\n")
        elif computer_action == "wolf":
            print("The wolf takes chase to the bun, but the bun is too fast and makes it back to the den before it can be claimed as dinner. The wolf must go hungry this time. You win!\n")
        else:
            humanandbun_win_or_lose_actions = ["The human unknowingly plants a garden of lettuce and tomatoes ontop of an underground bunny tunnel system, allowing them easy access to the human's produce within months while being difficult to find and exterminate. You win!\n", "The human lays traps that ensnare the bun and its kin. You lose!\n"]
            computer_action_bun_vs_human = random.choice(humanandbun_win_or_lose_actions)
            print(computer_action_bun_vs_human)
    elif player_action == "corvid":
        if computer_action == "bee":
            print("Bee is eaten by the corvid! You win!\n")
        elif computer_action == "bun":
            print("The bun, while trying to cross the street, is spooked when the corvid swipes down at it, causing it to backtrack and get hit by a car. The corvid can now feed on the roadkill. You win!\n")
        elif computer_action == "corvid":
            element_battle("water corvid beats fire corvid",
                       "water corvid loses to ground corvid",
                       "water corvid beats air corvid",
                       "water corvid loses to air corvid",
                       "fire corvid loses to water corvid",
                       "fire corvid beats earth corvid",
                       "fire corvid beats air corvid",
                       "fire corvid loses to air corvid",
                       "earth corvid beats water corvid",
                       "earth corvid loses to fire corvid",
                       "earth corvid beats air corvid",
                       "earth corvid loses to air corvid", #why does this pop up after a tie between earth corvid vs earth corvid?
                       "air corvid beats water corvid",
                       "air corvid loses to water corvid",
                       "air corvid beats fire corvid",
                       "air corvid loses to fire corvid",
                       "air corvid beats earth corvid",
                       "air corvid loses to earth corvid")
        elif computer_action == "cat":
            print("Cat stalks and kills the corvid. You lose!\n")
        elif computer_action == "wolf":
            print("The wolf, after making a kill, reacts aggressively to the corvid which came down to try and scavange with the pack. The corvid becomes an appetizer to the meal. You lose!\n")
        else:
            humanandcorvid_win_or_lose_actions = ["Human destroys the corvid's natural habitat and it's forced to live in the city. You lose!\n", "Human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by a crazed corvid. You win!\n"]
            computer_action_corvid_vs_human = random.choice(humanandcorvid_win_or_lose_actions)
            print(computer_action_corvid_vs_human)
    elif player_action == "cat":
        if computer_action == "bee":
            print("Bee becomes aggitated when the cat decides to climb a tree that inhabits their home. When the cat steps on the hive to aid its ascent, the bee sends out the pheramones necessary to protect the hive. The cat flees quickly. You lose!\n")
        elif computer_action == "bun":
            print("Bun tests its luck and explores a yard that is highly protected by the cat. The cat makes simple work of the curious bun. You win!\n")
        elif computer_action == "corvid":
            print("Corvid is stalked and killed by the highly invasive cat. You win!\n")
        elif computer_action == "cat":
            element_battle("water cat beats fire cat",
                       "water cat loses to ground cat",
                       "water cat beats air cat",
                       "water cat loses to air  cat",
                       "fire cat loses to water cat",
                       "fire cat beats earth cat",
                       "fire cat beats air cat",
                       "fire cat loses to air cat",
                       "earth cat beats water cat",
                       "earth be loses to fire cat",
                       "earth cat beats air cat",
                       "earth cat loses to air cat",
                       "air cat beats water cat",
                       "air cat loses to water cat",
                       "air cat beats fire cat",
                       "air cat loses to fire cat",
                       "air cat beats earth cat",
                       "air cat loses to earth cat")
        elif computer_action == "wolf":
            print("Wolf steals the cat wandering it's territory for dinner. You lose!\n")
        else:
            humanandcat_win_or_lose_actions = ["Human domesticates the cat and makes it wear silly hats and posts pictures of the embarassing situation all over the internet. You lose!\n", "Human is infected with toxoplasmosis and becomes a slave to the cat. You win!\n"]
            computer_action_cat_vs_human = random.choice(humanandcat_win_or_lose_actions)
            print(computer_action_cat_vs_human)
    elif player_action == "wolf":
        if computer_action == "bee":
            print("Bee stings the wolf in the muzz and it looks silly the rest of the day. You lose!\n")
        elif computer_action == "bun":
            print("Bun, while being chased by the wolf, leads it directly into the pathway of hunters before disappearing beneath the ground. The wolf must now outrun gunfire, as the wolf is no longer protected by a status of being endangered. You lose!\n")
        elif computer_action == "corvid":
            print("Corvid befriends the wolf and alerts it to prey for both to enjoy. You win!\n")
        elif computer_action == "cat":
            print("Cat navigates the forest and is stolen by the wolf for dinner. You win!\n")
        elif computer_action == "wolf":
            element_battle("water wolf beats fire wolf",
                       "water wolf loses to ground wolf",
                       "water wolf beats air wolf",
                       "water wolf loses to air  wolf",
                       "fire wolf loses to water wolf",
                       "fire wolf beats earth wolf",
                       "fire wolf beats air wolf",
                       "fire wolf loses to air wolf",
                       "earth wolf beats water wolf",
                       "earth be loses to fire wolf",
                       "earth wolf beats air wolf",
                       "earth wolf loses to air wolf",
                       "air wolf beats water wolf",
                       "air wolf loses to water wolf",
                       "air wolf beats fire wolf",
                       "air wolf loses to fire wolf",
                       "air wolf beats earth wolf",
                       "air wolf loses to earth wolf")
        else:
            humanandwolf_win_or_lose_actions = ["Human tests the wolf's boundaries with a meat-suit and gets mauled. You win!\n", "Human confuses coyotes killing their livestock for wolves and goes on a mass hunting spree. You lose!\n"]
            computer_action_wolf_vs_human = random.choice(humanandwolf_win_or_lose_actions)
            print(computer_action_wolf_vs_human)
    elif player_action == "human":
        if computer_action == "bee":
            bee_win_or_lose_actions = ["Bee does a little dance that rallies the masses to attack the human. You lose!\n", "Human makes a movie about the bee that makes everyone assume it likes Jazz. It hears 'Ya like jazz?' for the remainder of its life. You win!\n"]
            computer_action_human_vs_bee = random.choice(bee_win_or_lose_actions)
            print(computer_action_human_vs_bee)
        elif computer_action == "bun":
            bun_win_or_lose_actions = ["Bun, and its family, enjoys a very large meal which, to the human's dismay, turns out to be their crop yeild for the season. You lose!\n", "Bun foregoes it's usual choice of lettuce, and other mediocre looking vegetables, for some unusually juicy and delicious looking tomatoes. Turns out the reason they looked so good was because of DDT. The bun is poisoned and no longer bothers any of the crops. You win!\n"]
            computer_action_human_vs_bun = random.choice(bun_win_or_lose_actions)
            print(computer_action_human_vs_bun)
        elif computer_action == "corvid":
            corvid_win_or_lose_actions = ["Corvid drops from the sky due to human neonicotinoids. Well, at least the bugs are gone from the apples. You win!\n", "Corvid waits for human to turn its head then attacks while its not looking, you lose!\n"]
            computer_action_human_vs_corvid = random.choice(corvid_win_or_lose_actions)
            print(computer_action_human_vs_corvid)
        elif computer_action == "cat":
            cat_win_or_lose_actions = ["Human adopts the cat and realizes putting forth effort for another individual is too much. The cat is dumped in the street. You win!\n", "Cat, while being driven out of its home by someone who can no longer provide for it, turns and mauls the human with claws of fury before finding a better home elsewhere. You lose!\n"]
            computer_action_human_vs_cat = random.choice(cat_win_or_lose_actions)
            print(computer_action_human_vs_cat)
        elif computer_action == "wolf":
            wolf_win_or_lose_actions = ["Human retracts laws against indiscriminatory hunting of wolves. Wolves go extinct and species that require a keystone species destroy the ecosystem. You win!\n", "Human attempts to hunt a wolf and instead meets the whole pack. The human is out of ammo. You lose!\n"]
            computer_action_human_vs_wolf = random.choice(wolf_win_or_lose_actions)
            print(computer_action_human_vs_wolf)
        else:
            print("this is human vs human which are both wild cards, this will be substantially different from the function we've made.") #this point must be accomodated
    else: 
        #need this to restart the game and not lead to asking to play the game again
        print("Wait... what? Please check your spelling, capitalization, and make sure you're choosing an animal from the list of options. \n")
        #I think there is a way to make it so your spelling and capitalization matters less, but lets go with this for now
            
    while True:
        play_again = input("Play again? (y/n): ")    
        if play_again == "y":
            print ("\nRestarting...")
            break
        elif play_again == "n":
            print ("\nQuitting...\n")
            break
        elif play_again != "y":
            print ("\nI'm sorry. I don't understand. Please enter a lowercase y for Yes or a lowercase n for No.\n")
        elif play_again != "n":
            print ("\nI'm sorry. I don't understand. Please enter a lowercase y for Yes or a lowercase n for No.\n")

    if play_again == "n":
        break