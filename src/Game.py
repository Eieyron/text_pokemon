from classes.Pokemon import Pokemon
from classes.Item import Item

def main():

    string = ""

    pokemon_list = []

    print("Hello user, please enter pokemon 1 attributes.")

    pokemon_list.append(
        Pokemon(
            name = input("enter pokemon name: "), 
            # health = int(input("enter pokemon health: ")),
            # speed = int(input("enter pokemon speed: "))
        )
    )

    # pokemon_list[0].show_state()

    print("Hello user, please enter pokemon 2 attributes.")

    pokemon_list.append(
        Pokemon(
            name = input("enter pokemon name: "), 
            # health = int(input("enter pokemon health: ")),
            # speed = int(input("enter pokemon speed: "))
        )
    )

    # foreach loop
    for pokemon in pokemon_list:
        pokemon.show_state()

    print("LET THE BATTLE BEGIN")

    first_pokemon = (
        pokemon_list[0] if pokemon_list[0].speed > pokemon_list[1].speed else pokemon_list[1]
    )
    second_pokemon = (
        pokemon_list[0] if pokemon_list[1].speed > pokemon_list[0].speed else pokemon_list[1]
    )

    while first_pokemon.health > 0 and second_pokemon.health > 0:
        
        # first pokemon turn

        # get user input
        user_input_1 = int(input(string.join((
            "select what ",first_pokemon.name," will do.\n",
            "[0] attack\n",
            "[1] defend\n",
            "[2] run\n>>> ",
        ))))

        # second pokemon turn

        # get user input
        user_input_2 = int(input(string.join((
            "select what ",second_pokemon.name," will do.\n",
            "[0] attack\n",
            "[1] defend\n",
            "[2] run\n>>> ",
        ))))



        # process user input
        if user_input_1 == 0:
            first_pokemon.attack(second_pokemon)
        elif user_input_1 == 1:
            first_pokemon.defend()
        elif user_input_1 == 2:
            first_pokemon.run()

        # process user input
        if user_input_2 == 0:
            second_pokemon.attack(first_pokemon)
        elif user_input_2 == 1:
            second_pokemon.defend()
        elif user_input_2 == 2:
            second_pokemon.run()


        # show effects
        for pokemon in pokemon_list:
            pokemon.show_state()


    print("end of program")

main()