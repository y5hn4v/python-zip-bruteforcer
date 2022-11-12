
# Zip File Password Bruteforcer Made in Python
# Author : y5hn4v (https://github.com/y5hn4v)
# Version : 1.0.0
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

    plist = args.PasswordList
    zip_file = args.ZipFile
    save_file = args.s

    if save_file == "":
        save_file = os.getcwd() #Getting the current working directory

    zp = zipfile.ZipFile(zip_file)

    if zipfile.BadZipFile == True: #Checking if the file is zip
        print("It is not a zip file. Exiting program")
        exit()
    else:
        control = False
        print('Starting BruteForce: \n')
        with open(plist, 'rb') as file:
            if os.path.getsize(plist) == 0: #The password list is empty
                print("Please provide values in the password list you provided.Exiting program")
                exit()
            else:
                for password in file:
                    try:
                        zp.extractall(pwd = password[:-1], path=save_file)
                        print(f'Found password : {password.decode()}')
                        control = True
                        quit()
                    except Exception as e:
                        pass
                if control == False:
                    print("Password not detected in the password list ")

            

if __name__ == '__main__':
    main()

 