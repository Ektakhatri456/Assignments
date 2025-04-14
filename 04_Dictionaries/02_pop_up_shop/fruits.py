# Program 3: Fruits Shop
#Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    Fruits = {
        "apple" : 1.50,
        "mango" : 2.00,
        "strawberries" : 6.00,
        "kiwi" : 3.00,
        "cherries" : 4.00,
        }

    total_cost = 0
    for fruit_name in Fruits:
        price = Fruits[fruit_name]
        amount_bought = int(input("How many " + fruit_name + " do you want to buy? "))
        total_cost += price * amount_bought

    print("The total cost of all the fruits is: $" + str(total_cost))

if __name__ == "__main__":
    main()