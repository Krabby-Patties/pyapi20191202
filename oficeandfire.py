#!/usr/bin/python3

import requests

AOIFBOOK = 'https://anapioficeandfire.com/api/books'

def main():
    gotresp = requests.get(AOIF_BOOK)
    got_dj = gotresp.json()
    #print (got_dj_)

    # for singlebook in got_dj:
    #    print(f'{singlebook["name"]}, pages - {singlebook["numberofPages"]}')


var1 = "test"
var2 = "test2"

print(f'1st var is {var1} 2nd var is {var2}')


if __name__ == "__main__":
    main()