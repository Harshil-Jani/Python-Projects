# Made by Harshil Jani
import os
def main():
    path = input("Write Directory Path : ")
    extension = input("To What extension would you like to change the file : ")
    for filename in os.listdir(path):
        temp = path + filename 
        pos = filename.rfind('.') 
        filename = filename[:pos] 
        my_file = path + filename + extension
        os.rename(temp,my_file)
if __name__ == '__main__':
    main()

