#!/usr/bin/python3

import json
import urllib.request

NEO = "https://api.nasa.gov/neo/rest/v1/feed?api_key="


def main():
    ## Get my API key - r is RAW string --- the second r is READ
    with open(r"C:\Users\Pinad\Documents\nasacreds.txt", "r") as nc:
        myapikey = nc.read()

    ##make a request to NEO and save resp as neoresp
    neoresp = urllib.request.urlopen(NEO + myapikey)
    ## strip off ATTACHED json data and save as neojson
    neojson = neoresp.read().decode("utf-8")
    print(type(neojson))  ## this returns bytes UNTIL we .decode
    ## now it is returning str

    neopy = json.loads(neojson)  # translate string to dict

    for nasadate in neopy["near_earth_objects"]:
        print(nasadate)

    for astroids in neopy["near_earth_objects"]["2019-12-08"]:
        #print(astroids["id"])
        #print(astroids["name"])
        print("The human name is: ", astroids["name"])
        print("The Astronmical ID is: ", astroids["id"])
        print("The speed of this astroid is: ", astroids["close_approach_data"][0]["relative_velocity"]['miles_per_hour'], "miles per hour"),
        print()
if __name__ == "__main__":
    main()
