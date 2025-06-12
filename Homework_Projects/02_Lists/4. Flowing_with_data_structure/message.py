# Program 4: Mutable and Immutable data types differentiation.


# Function jo diye gaye data ki 3 copies list mein add karega
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)  # Yeh list ko seedha modify karta hai (mutable operation)

def main():
    # User se message input lene ka prompt
    message = input("Enter a message to copy: ")  # Yeh ek immutable data type hai (string), jo mutable list mein pass ho raha hai

    my_list = []  # Ek khali list banayi gayi hai (mutable data type)

    print("List before:", my_list)  # Function call se pehle list print karte hain (abhi khali hai)

    add_three_copies(my_list, message)  # Function ko call karke hum list ko directly modify kar rahe hain

    # List ko print karte hain function call ke baad, taake changes dikh sakein
    print("List after:\n" + "\n".join(my_list))  # List ko modify kiya gaya hai, kyunki function ne usay directly change kiya

# Yeh ensure karta hai ke main() sirf tab chale jab yeh file directly execute ho, na ke jab yeh kisi aur file mein import ki jaye
if __name__ == "__main__":
    main()  # Yeh sirf tab run hoga jab yeh script directly execute ho, na ke jab yeh import ki jaye
