# Program 3: to check if a number is within a given range
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n, low, high):

    """ Returns True if n is between low and high, inclusive. """
    return low <= n <= high

print(in_range(10, 10, 20))
print(in_range(5, 10, 20))




