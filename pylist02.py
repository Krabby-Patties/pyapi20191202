#!/usr/bin/python3

def main():
    ##create an empty list
    mylist = []

    ## open a SLOT at the END of the list to ADD the value
    mylist.append("monday")

    mylist.append("tuesday")

    mylist.append("wednesday")

    mylist.append("thursday")

    print(mylist)

    print(mylist[0])
    print(mylist[3])

    ##we  want to create an empty dictionary
    studiomovies ={}

    ##we want to create the KEY pixar and map to a value

    studiomovies["pixar"] = "toystory"

    studiomovies["universal"] = "jaws"

    studiomovies["paramaount"] = "raiders of lost ark"

    print(studiomovies)

    print(studiomovies["paramaount"])

    studiomovies["pixar"] = "up"

    print(studiomovies["pixar"])

    ## map studiomoviespixar to a LIST

    studiomovies["pixar"] = ["toy story", "up"]

    print(studiomovies["pixar"][1])

    studiomovies
if __name__ == "__main__":
    main()