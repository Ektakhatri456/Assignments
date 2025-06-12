# Program 4: Password Manager
#You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

#This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
#For example, using a hash function called SHA256(...) something as simple as  hello
#can be hashed into a much more complex: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
#Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
#(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)



from hashlib import sha256
def login(email, stored_logins, password_to_check):
    """
    This function checks if the given password matches the stored on (after hashing).

    Parameters used:
    email (str): The email of the user to find the stored password for.
    stored_logins (dict): Dictionary with emails as keys and hashed passwords as values.
    password_to_check (str): Password entered by the user for login.

    Returns:
    bool: True if the password matches, otherwise false.

    """

#Check if the hash of the stored password matches the stored password
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    """
    Converts the input password into a secure hash SHA256. 

    Parameters:
    password (str): The original password to be hashed.

    Returns:
    str: The hashed encrypted version of the password.
    
    """

    return sha256(password.encode()).hexdigest()  #Encode the password and hash it.

def main():
    #Dictionary to store email and corresponding hashed password

    stored_logins = {
        "example@gmail.com" : "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_place@cip.org" : "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu" :  "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"

    }

    #Testing different login scenarios

    print(login("example@gmail.com", stored_logins, "word"))      #False - wrong password
    print(login("example@gmail.com", stored_logins, "password"))  #True -  correct password

    print(login("code_in_place@cip.org", stored_logins, "Karel"))   #False - wrong password
    print(login("code_in_place@cip.org", stored_logins, "karel"))    #True - correct password

    print(login("student@stanford.edu", stored_logins, "password"))      #False - wrong password
    print(login("student@stanford.edu", stored_logins, "123!456?789"))    #True - correct password


if __name__ == "__main__":
    main()


    