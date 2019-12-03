#!/usr/bin/python3

def main():
    myname = "Jose" #string
    myage = 20 #int
    mypets = ["Charlie", "Penny", "Pepe"] #list

    #this WILL work (this is called concatination)
    print(myname + " is the student.") ## < Jose is the student. >

    #this will NOT work ( cannot ADD apples and oranges...)
    #print( myname + "is" + myage) ## < error >

    #this WILL work (we changed an orange into an apple!)
    print(myname + " is " + str(myage))  ## < Jose is 20 >

    # We can also print a series of objects regardless of their type ( like distributing in PEMDAS )
    print(myname, "is", myage)  ## < Jose is 20 >

    # f strings can be used ANYWHERE! including inside the print()
    print(f'My name, {myname}, was given to me {myage} years ago.')

    mystring = f"The name of my pets are {mypets[0]}, the dog, {mypets[2]} " \
               f"my pet bird, and finally {mypets[1]}, surprise, is another pet"

    mystring = f"My pets are {mypets[0]}, the dog, {mypets[2]} the other cat, " \
               f"and finally {mypets[1]}, surprise is another pet."

    print(mystring)


    print("Zach says {} are another way to do this. I think he is a {}".format("format strings", "really smart guy"))

    x = 1955
    y = "Nov 05"

    # with a format string the {} {} values are {0} and {1} implied
    print("Doc Brown invented time travel on {}, {}".format(y,x))

    # if we want we can hardcode the int found inside {}
    print("Doc Brown invented time travel on {1}, {0}".format(y, x))

    # here we UNPACK the list called mypets by placing a SPLAT aka '*' before the list
    print("My pets are {} {} {}".format(*mypets))

if __name__ == "__main__":
    main()