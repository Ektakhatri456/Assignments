# Program 06: Even or Odd Identifier from 10 to 19

def is_odd(value : int):
    remainder = value % 2
    return remainder == 1

def main():
    for i in range(10, 30):
        if is_odd(i):
            print(f"{i} is odd", end = " ")
        else:
            print(f"{i} is even", end = " ")

if __name__ == "__main__":
    main()
