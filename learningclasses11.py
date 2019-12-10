#!/usr/bin/python3
import json
class Mariokartplayer:
    def __init__(self, name, karttype):
        with open("mkcharacters.json") as mkd:
            stats = json.load(mkd)
        self.name = name             # player selected character
        self.karttype = stats[name]["type"]     # the kart type selected
        self.score = 0               # current score
        self.item = None             # item character has picked up
        self.type = stats[name]["type"]
    ## this is for display
    def __str__(self):
        return self.name
    def scorechange(self,x):
        self.score += 10

def main():
    print("Learning about classes with Mario Kart")
    player1 = Mariokartplayer("Baby Mario", type)

    print(player1)  ## this reveals the def __str__:
    print(player1.name)
    print(player1.karttype)
    print(player1.score)
    print(player1.item)
    print(player1.type)
    ## in our game... player1 just touched a coin
    player1.scorechange("coin")
    print(player1.score)
    player1.scorechange("finishline")
    print(player1.score)
    player1.scorechange("pollywollydoodle")
    print(player1.score)

main()