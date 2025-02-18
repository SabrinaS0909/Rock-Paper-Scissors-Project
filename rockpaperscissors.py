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
    #... gets stung in the muzz and looks silly the rest of the day. You win!

    print(f"\nIt's {player_action} vs {computer_action}.\n")

    if player_action == computer_action:
        #This one is where the differentiating mechanics come in. And the game goes deeper.
        print(f"Both players selected {player_action}. It's a tie!! ... for now.\n") #change the dialogue here once you add in the additional mechanics
    elif player_action == "bee":
        if computer_action == "bun":
            print("... You lose!\n") # needs dialogue added
        elif computer_action == "corvid":
            print("Corvid eats the bee. You lose!\n")
        elif computer_action == "cat":
            print("... You win!\n") # needs dialogue added
        elif computer_action == "wolf":
            print("... You win!\n") # needs dialogue added
        else:
            humanandbee_win_or_lose_actions = ["Human is allergic to the bee and is hospitalized. You win!\n", "Human smacks the bee with a newspaper, crushing it immediately. You lose!\n"]
            computer_action_bee_vs_human = random.choice(humanandbee_win_or_lose_actions)
            print(computer_action_bee_vs_human)
    elif player_action == "bun":
        if computer_action == "bee":
            print("You win!\n") #needs dialogue added
        elif computer_action == "corvid":
            print("You lose!\n") #needs dialogue added
        elif computer_action == "cat":
            print("You lose!\n") #needs dialogue added
        elif computer_action == "wolf":
            print("You win!\n") #needs dialogue added
        else:
            humanandbun_win_or_lose_actions = ["You win!\n", "You lose!\n"] #needs dialogue added
            computer_action_bun_vs_human = random.choice(humanandbun_win_or_lose_actions)
            print(computer_action_bun_vs_human)
    elif player_action == "corvid":
        if computer_action == "bee":
            print("Bee is eaten by the corvid! You win!\n")
        elif computer_action == "bun":
            print("You win!\n") #needs dialogue added
        elif computer_action == "cat":
            print("Cat stalks and kills the corvid. You lose!\n")
        elif computer_action == "wolf":
            print("You lose!\n") #needs dialogue added
        else:
            humanandcorvid_win_or_lose_actions = ["Human destroys the corvid's natural habitat and it's forced to live in the city. You lose!\n", "Human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by a crazed corvid. You win!\n"]
            computer_action_corvid_vs_human = random.choice(humanandcorvid_win_or_lose_actions)
            print(computer_action_corvid_vs_human)
    elif player_action == "cat":
        if computer_action == "bee":
            print("You lose!\n") #needs dialogue added
        elif computer_action == "bun":
            print("You win!\n") #needs dialogue added
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
            print("You lose!\n") #needs dialogue added
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
            bun_win_or_lose_actions = ["You lose!\n", "You win!\n"] #need dialogue
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

