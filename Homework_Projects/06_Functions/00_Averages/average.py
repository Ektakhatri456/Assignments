# Program 1: Calculating average of two numbers.
#Question:
# Write a function that takes two numbers and finds the average between the two.

def average(a : float, b : float):
    avg = (a + b) / 2
    return avg

def main():
    avg_1 = average(10, 20)
    avg_2 = average(5, 15)
    final_avg = average(avg_1, avg_2)

    print("Average-1:", avg_1)
    print("Average-2:", avg_2)
    print("Final Average:", final_avg)

if __name__ == "__main__":
    main()