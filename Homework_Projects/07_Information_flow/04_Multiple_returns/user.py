# Program 5: Website Sign-Up Data Collector

def get_user_info():
    first_name : str = input("What is your first name?: ")
    last_name : str = input("What is your last name?: ")
    email : str = input("What's your email address?: ")

    return first_name, last_name, email

def main():
    user_data = get_user_info()
    print("Received the following user data: ", user_data)

if __name__ == "__main__":
    main()


