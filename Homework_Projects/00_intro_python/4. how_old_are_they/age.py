#Program 4: How old are they

#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
#Anton is 21 years old.
#Beth is 6 years older than Anton.
#Chen is 20 years older than Beth.
#Drew is as old as Chen's age plus Anton's age.
#Ethan is the same age as Chen.
#Your code should store each person's age to a variable and print their names and ages at the end. 
#The autograder is sensitive to capitalization and punctuation, be careful! 
#Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

def main():
    Anton : int = 21
    Beth : int = Anton + 6
    Chen : int= Beth + 20
    Drew : int = Chen + Anton
    Ethan : int = Chen

    print("Anton is " + str(Anton) + " years old.")
    print("Beth is " + str(Beth) + " years old.")
    print("Chen is " + str(Chen) + " years old.")
    print("Drew is " + str(Drew) + " years old.")
    print("Ethan is " + str(Ethan) + " years old.")

if __name__ =="__main__":
    main()