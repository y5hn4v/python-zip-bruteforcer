
# Zip File Password Bruteforcer Made in Python
# Author : y5hn4v (https://github.com/y5hn4v)
# Version : 1.1.0
# For educational purpose only
# To display the help message : python bruteforcer.py -h


import zipfile
import argparse
import os


def main():
    #argparse for the CLI
    parser = argparse.ArgumentParser(description="A .zip file password bruteforcer built in python")

    parser.add_argument("ZipFile", metavar="ZipFile", type=str, help="Path to the zip file")
    parser.add_argument("PasswordList", metavar="PasswordList", type=str, help="Path to the password list")
    parser.add_argument("-s", metavar="Extract/to/path", type=str, help="Path to extract the zip file.If not provided, the file will be extracted to current working directory")

    args = parser.parse_args()
    
    #File locations and the save path
    plist = args.PasswordList
    zip_file = args.ZipFile
    save_file = args.s
    
    #Below conditions check if the file or the path exists in the users computer
    if os.path.exists(zip_file) == False:
        print("Zip File not found")
        exit()
    if os.path.exists(plist) == False:
        print("The password list is not found")
        exit()
    #If the user didnt specify a path to extract the zip
    if save_file == None: 
        save_file = os.getcwd() #Getting the current working directory
    if os.path.exists(save_file) == False:
        print("The path to save location does not exists")
        exit()
   
    try:
        # If the file is actually a zip file this code with execute
        with zipfile.ZipFile(zip_file) as zp: 
            control = False
            print('Starting BruteForce: \n')
            with open(plist, 'rb') as file:
                if os.path.getsize(plist) == 0: #The password list is empty
                    print("Please provide values in the password list you provided.Exiting program")
                    exit()
                else:
                    # Looping through each password in the list
                    for password in file: 
                        try:
                            zp.extractall(pwd = password[:-1], path=save_file)
                            print(f'Found password : {password.decode()}')
                            control = True
                            quit()
                        except Exception as e: # Password didnt match 
                            pass
                    if control == False:
                        print("Password not detected in the password list ")
    except zipfile.BadZipFile: # The file is not a zip file
        print("The file is not a zipfile")
        exit()
        
            

if __name__ == '__main__':
    main()

 
