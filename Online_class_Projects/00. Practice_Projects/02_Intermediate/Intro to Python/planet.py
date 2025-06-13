# Program: Planetary Weight Converter

#Milestone 1: Mars Weight Calculator
def main():

    earth_weight = float(input("Enter your weight on Earth: "))
    mars_factor = 0.378

    mars_weight = earth_weight * mars_factor
    mars_weight = round(mars_weight, 2)

    print("The equivalent on Mars", mars_weight)


#Milestone 2: Planetary Weight Calculator
    planet = input("Enter a planet: ")

    if planet.lower() == "mercury":
        factor = 0.376
    elif planet.lower() == "venus":
        factor = 0.889
    elif planet.lower() == "mars":
        factor = 0.378
    elif planet.lower() == "jupiter":
        factor = 2.36
    elif planet.lower() == "saturn":
        factor = 1.081
    elif planet.lower() == "uranus":
        factor = 0.815
    elif planet.lower() == "neptune":
        factor = 1.14
    else:
        print("Invalid planet name.")
        exit()

    planet_weight_2 = earth_weight * factor
    planet_weight_2 = round(planet_weight_2, 2)

    print(f"The equivalent weight on {planet}: {planet_weight_2}.")

if __name__ == "__main__":
    main()









   