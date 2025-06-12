# Program 4: Pythagorean theorem
# This program calculates the length of the hypotenuse of a right angled triangle.

#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle
# and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

#Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC).
#  You will probably find math.sqrt() to be useful.

import math
def main():
    SIDE_AB = float(input("Enter the length of Perpendicular (AB): "))
    SIDE_AC = float(input("Enter the length of Base (AC): "))
    SIDE_BC = math.sqrt(SIDE_AB ** 2 + SIDE_AC ** 2)

    print(f"The Length of Hypotenuse (BC) is: {SIDE_BC:.2f}")

if __name__ == "__main__":
    main()