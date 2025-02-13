"""This is a small project of my own take on a game of Rock, Paper, Scissors"""

import random

"""So, this is where I want to decide how to implement my own twist on a very classic game.
I can choose the same gameplay just with my own name for everything, but I feel that would be boring.
Can I implement at least one more twist on things. To the mechanics, maybe.
We can add more objects, for example if we have rock, paper scissors, then we can add in more objects that interact with the current objects in meaningful ways. Let's aim for two of these.
Then, maybe, we could add in some sort of wildcard. A new mechanic. Maybe a tie breaker, even. Maybe if two choose the same object initially, it decends into a secondary game. And maybe even from there a thrid or fourth if the luck were so.
So we've gotta choose something large, then scope in at least four times.
I'm thinking three creatures, then three elements, then going into composition of their matter (solid, gas and liquid), then from there... hmm.
Then, lastly, neutron, proton and electrons feels like the most obvious place to go from there. 
Another factor could be age. That could be a more simple dynamic, that plays better with what common people are down to deal with."""

"""Now to keep mistakes from happening, I need to change the objects to my own and maintain, rather than putting in rock, paper and scissors and potentially missing replacing one.
I think the animal that is the "weakest" but can also take out the strongest should be a bee.
So bee = paper, then raven eats the bee and is therefore scissors, then maybe a cat - then because I want to extend it out a little bit, let's add two more animals and see if it overcomplicated the coding process.
Maybe wolf, then human. But the human can get stung by the bee and therefore loses to the bee."""

player_action = input("Enter your animal of choice: Bee, Corvid, Cat, Wolf, Human\n")
#when we put css in, I would like to add pictures of the animals of choice that the player can choose from. Maybe even randomize the photo shown each playthrough.
possible_actions = ["bee", "corvid", "cat", "wolf", "human"]
computer_action = random.choice(possible_actions)

print(f"\nIt's {player_action} vs {computer_action}.\n")

if player_action == computer_action:
    #This one is where the differentiating mechanics come in. And the game goes deeper.
elif player_action == "bee":
    if computer_action == "corvid":
        print("Corvid eats the bee! You lose!")
    elif computer_action == "cat":
        print("Cat paws the bee to death, you lose!")
    elif computer_action == "wolf":
        print("Wolf gets stung in the muzz and looks silly the rest of the day. You win!")
    else:
        print("Human is allergic to the bee and is hospitalized. You win!")
elif player_action == "corvid":
    if computer_action == "bee":
        print("Bee is eaten by the corvid! You win!")
    elif computer_action == "cat":
        print("Cat stalks and kills its prey, you lose!")
    elif computer_action == "wolf":
        print("Wolf befriends the corvid and they hunt prey together, you win!")
    else:
        print("Human destroys the corvid's natural habitat and it's forced to live in the city. You lose!")
elif player_action == "cat":
    if computer_action == "bee":
        print("Bee gets pawed to death by cat! You win!")
    elif computer_action == "corvid":
        print("Corvid is stalked and killed by the highly invasive cat. You win!")
    elif computer_action == "wolf":
        print("Wolf steals the cat wandering it's territory for dinner. You lose!")
    else:
        print("Human domesticates cat and makes it wear silly hats and posts pictures of the embarassing situation all over the internet. You lose!")
elif player_action == "wolf":
    if computer_action == "corvid":
        print("Corvid befriends the wolf and alerts it to prey for both to enjoy. You win!")
    elif computer_action == "cat":
        print("Cat navigates the forest and is stolen by wolf for dinner. You win!")
    elif computer_action == "bee":
        print("Bee stings wolf in the muzz and it looks silly the rest of the day. You lose!")
    else:
        print("Human tests wolf boundaries with a meat-suit and gets mauled. You win!")
#what if we made the human a wild card where it could be randomized that you could win or lose
elif player_action == "human":
    if computer_action == "corvid":
        corvid_win_or_lose_actions = ["Corvid drops from the sky due to human neonicotinoids. Well, at least the bugs are gone from its apples. You win!", "Corvid waits for human to turn its head then attacks while its not looking, you lose!"]
        computer_action_human_vs_corvid = random.choice(human_win_or_lose_actions)
        print(computer_action_human_vs_corvid)
    elif computer_action == "cat":
        cat_win_or_lose_actions = ["", ""]
        computer_action_human_vs_cat = random.choice(cat_win_or_lose_actions)
        print(computer_action_human_vs_cat)
    elif computer_action == "wolf":
        wolf_win_or_lose_actions = ["", ""]
        computer_action_human_vs_wolf = random.choice(wolf_win_or_lose_actions)
        print(computer_action_human_vs_wolf)
    else:
        bee_win_or_lose_actions = ["", ""]
        computer_action_human_vs_bee = random.choice(bee_win_or_lose_actions)
        print(computer_action_human_vs_bee)

