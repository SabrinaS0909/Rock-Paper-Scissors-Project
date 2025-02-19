"""This is a small project of my own take on a game of Rock, Paper, Scissors"""

# I want to have each scenario be unique though, when a wolf wins against the cat I want the scenario to be creatively different for when the cat loses against the wolf

import random

while True:
    player_action = input("\nEnter your animal of choice: bee, bun, corvid, cat, wolf, human\n")
    # when we put css in, I would like to add pictures of the animals of choice that the player can choose from. Maybe even randomize the photo shown each playthrough.
    possible_actions = ["bee", "bun", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)

    # I like these:
    #... sensitive ears pick up the cautionary buzz of the bee and is terrified into running back home. You win!

    print(f"\nIt's {player_action} vs {computer_action}.\n")

    if player_action == computer_action:
        #This one is where the differentiating mechanics come in. And the game goes deeper.
        print(f"Both players selected {player_action}. It's a tie!! ... for now.\n") #change the dialogue here once you add in the additional mechanics
    elif player_action == "bee":
        if computer_action == "bun":
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
        else:
            wolf_win_or_lose_actions = ["Human retracts laws against indiscriminatory hunting of wolves. Wolves go extinct and species that require a keystone species destroy the ecosystem. You win!\n", "Human attempts to hunt a wolf and instead meets the whole pack. The human is out of ammo. You lose!\n"]
            computer_action_human_vs_wolf = random.choice(wolf_win_or_lose_actions)
            print(computer_action_human_vs_wolf)
    else: 
        print("Wait... what? Please check your spelling, capitalization, and make sure you're choosing an animal from the list of options. \n")
        #I think there is a way to make it so your spelling and capitalization matters less, but lets go with this for now
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

