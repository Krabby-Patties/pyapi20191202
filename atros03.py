#!/usr/bin/python3

ASTROS = {"people": [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}], "number": 6, "message": "success"}

def main():
    ## you write code under here
    ## display Christina Koch
    print(ASTROS["people"][0]["name"])
    ##display Alexander
    print(ASTROS["people"][1]["name"])

    print(ASTROS["people"][2]["name"])

    print(ASTROS["people"][3]["name"])

    print(ASTROS["people"][4]["name"])

    print(ASTROS["people"][5]["name"])

    ## intro to looping loop across the list mapped to PEOPLE in ASTROS
    for poi in ASTROS["people"]:
        print(poi["name"], "is riding on the", poi["craft"]) ## this is prob 2 much info I JUST want name key

if __name__ == "__main__":
    main()