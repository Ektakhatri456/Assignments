# Program 2: Einstein's mass energy equation
#Write a program that continually reads in mass from the user and then outputs the equivalent energy 
# using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, 
# and C is the speed of light:

#E = m * c**2
#Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable 
# and are related by the above equation. You should ask the user for mass (m) in kilograms 
# and use a constant value for the speed of light -- C = 299792458 m/s.

def calculate_energy(mass):
    C = 299792458 # Speed of light in m/s
    energy = mass * C**2
    return energy

def main():
    while True:
        user_input = input("Enter mass in kilograms (or 'exit' to quit): ")
        if user_input.lower() == 'exit': # Allow user to exit the program
            print("Exiting the program...")
            break
        try:
            mass = float(user_input)
            energy = calculate_energy(mass)
            print(f"\ne = m * C ^ 2...")
            print(f"m = {mass} kg")
            print(f"C = {299792458} m/s")
            print(f"{energy:.2e} Joules of energy\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value for mass.")

if __name__ == "__main__":
    main()