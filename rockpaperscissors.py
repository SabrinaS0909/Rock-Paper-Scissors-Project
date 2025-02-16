"""This is a small project of my own take on a game of Rock, Paper, Scissors"""

#we need to add in one more animal, because making the human a wild card has made the guaranteed wins vs loses uneven

import random

while True:
    player_action = input("Enter your animal of choice: bee, corvid, cat, wolf, human\n")
    #when we put css in, I would like to add pictures of the animals of choice that the player can choose from. Maybe even randomize the photo shown each playthrough.
    possible_actions = ["bee", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)

    print(f"\nIt's {player_action} vs {computer_action}.\n")

    if player_action == computer_action:
        #This one is where the differentiating mechanics come in. And the game goes deeper.
        print(f"Both players selected {player_action}. It's a tie!! ... for now.\n")
    elif player_action == "bee":
        if computer_action == "corvid":
            print("Corvid eats the bee! You lose!\n")
        elif computer_action == "cat":
            print("Cat paws the bee to death, you lose!\n")
        elif computer_action == "wolf":
            print("Wolf gets stung in the muzz and looks silly the rest of the day. You win!\n")
        else:
            humanandbee_win_or_lose_actions = ["Human is allergic to the bee and is hospitalized. You win!\n", "Human smacks the bee with a newspaper, crushing it immediately. You lose!\n"]
            computer_action_bee_vs_human = random.choice(humanandbee_win_or_lose_actions)
            print(computer_action_bee_vs_human)
    elif player_action == "corvid":
        if computer_action == "bee":
            print("Bee is eaten by the corvid! You win!\n")
        elif computer_action == "cat":
            print("Cat stalks and kills the corvid, you lose!\n")
        elif computer_action == "wolf":
            print("Wolf befriends the corvid and they hunt prey together, you win!\n")
        else:
            humanandcorvid_win_or_lose_actions = ["Human destroys the corvid's natural habitat and it's forced to live in the city. You lose!\n", "Human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by a crazed corvid. You win!\n"]
            computer_action_corvid_vs_human = random.choice(humanandcorvid_win_or_lose_actions)
            print(computer_action_corvid_vs_human)
    elif player_action == "cat":
        if computer_action == "bee":
            print("Bee gets pawed to death by the cat! You win!\n")
        elif computer_action == "corvid":
            print("Corvid is stalked and killed by the highly invasive cat. You win!\n")
        elif computer_action == "wolf":
            print("Wolf steals the cat wandering it's territory for dinner. You lose!\n")
        else:
            humanandcat_win_or_lose_actions = ["Human domesticates the cat and makes it wear silly hats and posts pictures of the embarassing situation all over the internet. You lose!\n", "Human is infected with toxoplasmosis and becomes a slave to the cat. You win!\n"]
            computer_action_cat_vs_human = random.choice(humanandcat_win_or_lose_actions)
            print(computer_action_cat_vs_human)
    elif player_action == "wolf":
        if computer_action == "corvid":
            print("Corvid befriends the wolf and alerts it to prey for both to enjoy. You win!\n")
        elif computer_action == "cat":
            print("Cat navigates the forest and is stolen by the wolf for dinner. You win!\n")
        elif computer_action == "bee":
            print("Bee stings the wolf in the muzz and it looks silly the rest of the day. You lose!\n")
        else:
            humanandwolf_win_or_lose_actions = ["Human tests the wolf's boundaries with a meat-suit and gets mauled. You win!\n", "Human confuses coyotes killing their livestock for wolves and goes on a mass hunting spree. You lose!\n"]
            computer_action_wolf_vs_human = random.choice(humanandwolf_win_or_lose_actions)
            print(computer_action_wolf_vs_human)
    elif player_action == "human":
        if computer_action == "corvid":
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
            bee_win_or_lose_actions = ["Bee does a little dance that rallies the masses to attack the human. You lose!\n", "Human makes a movie about the bee that makes everyone assume it likes Jazz. It hears 'Ya like jazz?' for the remainder of its life. You win!\n"]
            computer_action_human_vs_bee = random.choice(bee_win_or_lose_actions)
            print(computer_action_human_vs_bee)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

