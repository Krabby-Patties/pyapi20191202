#!/usr/bin/python3

# JSON is part of the Python Standard Library
import json

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
                   {"name": "Arthur Dent", "species": "Human"}]

    ## display our python data ( a list containing dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguid.json", "w") as zfile:
        ## use the JSON library
        ## USASAGE: json.dump(input data, file like object) ##
        json.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()

