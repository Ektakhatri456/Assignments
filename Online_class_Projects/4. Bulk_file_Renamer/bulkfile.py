# Renaming Bulk files in a folder

import os

def main():
    i = 0
    path = "C:/Users/ekki1/OneDrive/Desktop/Online class_projects/Bulk_file_Renamer/images/"

    for file_name in os.listdir(path):
        my_dest = "image " + str(i) + ".jpg"
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()
