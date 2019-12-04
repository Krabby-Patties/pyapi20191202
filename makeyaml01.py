#!/usr/bin/python3

# YAML is not part of the standard library
# Python3 -m pip install pyyaml
import yaml
def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "sepcies": "Betelgeusian"}, \
                   {"name": "Arthur Dent", "species": "Human"}]
    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.yaml", "w") as zfile:

        ## use the YAML library
        ## USAGE: yaml.dump(input data, file like object)
        ## unlinke JSONm the YAML lib uses .dump() to
        ## create YAML strings and write to files
        ## the JSON lib uses .dump() to create a string and .dumps() ti write ti files
        yaml.dump(hitchhikers, zfile)

if __name__ == '__main__':
        main()