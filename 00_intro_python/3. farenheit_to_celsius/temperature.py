#Program 3: Farenheit to celsius

def main():
    degrees_fahrenheit = float(input("Enter the temperature in degrees Farenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

if __name__ == "__main__":
    main()    