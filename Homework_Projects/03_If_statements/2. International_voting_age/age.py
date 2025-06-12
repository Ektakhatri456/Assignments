# Program 2: Voting Eligibility Checker
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Peturksbouipo_age : int = 16
Stanlau_age : int = 25
Mayengua_age : int = 48

def main():
    user_age = int(input("Please enter your age: "))
    if user_age >= Peturksbouipo_age:
        print(f"You can vote in Peturksbouipo, where the voting age is {Peturksbouipo_age}.")
    else:
        print(f"You cannot vote in Peturksbouipo, where the voting age is {Peturksbouipo_age}.")
    
    if user_age >= Stanlau_age:
        print(f"You can vote in Stanlau, where the voting age is {Stanlau_age}.")
    else:
        print(f"You cannot vote in Stanlau, where the voting age is {Stanlau_age}.")

    if user_age >= Mayengua_age:
        print(f"You can vote in Mayegua, where the voting age is {Mayengua_age}.")
    else:
        print(f"You cannot vote in Mayengua, where the voting age is {Mayengua_age}.")

if __name__ == "__main__":
    main()

        


