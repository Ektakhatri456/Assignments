#Project 1: Mad libs python project

names = input("Names: ")
place = input("Place: ")
adj1 = input("Adjective 1: ")
adj2 = input("Adjective 2: ")
animal = input("Animal: ")
verb = input("Verb: ")
food = input("Food: ")
object = input("Object: ")

madlib = f"\nOne day, {names} went to {place}. It was very {adj1} day. Suddenly, a huge {animal} appeared and started to {verb}! \nShocked, {names} dropped their {food} and ran towards a {object} to hide. It was the most {adj2} day ever! "

print(madlib)