#!/usr/bin/python3

## this application is designed to generate poems from a dictionary (poems.json)

## import json to turn poems.json into pythonic
import json
import random

## step 1 open my poem database (poems.json)
with open("poems.json") as pj:
    pythonpoems = json.load(pj) ##convert poems.json data to pythonic structure

## randomly select a poem from pythonic data
print(random.choice(list(pythonpoems.values())))


## convert peoms.json data to pythonic data
## I think I can do this with import json

## randomly select a poem from the pythonic data
## I think i can do this with import random

