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

    ## Create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of YAML
    print(yamlstring)

if __name__ == '__main__':
    main()