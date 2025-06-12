# Program 4: Sophia's Fruit Store Inventory Checker

def main():
    fruit : str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print(f"Sorry, we are out of {fruit}.")
    else:
        print(f"This fruit is in stock. Here is how many: {stock}.")

def num_in_stock(fruit):
    if fruit == "apple":
        return 10
    elif fruit == "durian":
        return 15
    elif fruit == "pear":
        return 1000
    else:
        return 0
    
if __name__ == "__main__":
    main()
