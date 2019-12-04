#!/usr/bin/python3
## this is for pretty printing complex data
import pprint
## this is for priny
import requests

POKEMONAPI = "https://pokeapi.co/api/v2/pokemon/pikachu/"

def main():
    # go grab ALL the info from the API
    poke = requests.get(POKEMONAPI)
    # strip off the JSON from the API
    pokejson = poke.json()
    # loop across Just the abilities
    for abl in pokejson["abilities"]:
        # print JUST the ability name
         print(abl["ability"]["name"])

    # go loop across just the pokemon attack moves
    for atk in pokejson["moves"]:
        # print JUST the attack move names
        print(atk["move"]["name"])
    ## im trying to loop across mapped as "moves" > "move" > "name"
    ##for attacks in pokejson["moves"["move"]["name"]]
      ##  print(attacks)
if __name__ == '__main__':
    main()