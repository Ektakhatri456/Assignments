#Program 5: Triangle_perimeter

#Prompt the user to enter the lengths of each side of a triangle and then 
# calculate and print the perimeter of the triangle (the sum of all of the side lengths).

#Here's a sample run of the program (user input is in bold italics):

#What is the length of side 1? 3

#What is the length of side 2? 4

#What is the length of side 3? 5.5

#The perimeter of the triangle is 12.5

def main():
    length_1 : float = float(input("What is the length of 1st side? "))
    length_2 : float = float(input("What is the length of 2nd side? "))
    length_3 : float = float(input("What is the length of 3rd side? "))

    perimeter : int = length_1 + length_2 + length_3
    print("The perimeter of the triangle is", perimeter)



if __name__ == "__main__":
    main()    