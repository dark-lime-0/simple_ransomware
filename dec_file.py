import os
from cryptography.fernet import Fernet

# write a decryption script of the ransomware
# created by Youssef/dark-lime-0

def main()->None:
    files_to_dec=[]
    try:
        dir = input("specify a dir to decrypt : ")
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file == 'enc_file.py' or file =="thekey.key" or file == 'dec_file.py':
                    continue
                if os.path.isfile(file):
                    files_to_dec.append(file)
            print(files_to_dec)

        with open("thekey.key", 'rb') as thekey:    # save the decryption key in a variable
            key=thekey.read()

        for file in files_to_dec :                         # encrypt the plaintext data
            with open(file,'rb') as thefile:
                containts = thefile.read()
            dec_data = Fernet(key).decrypt(containts)
            with open(file, 'wb') as thefile :
                thefile.write(dec_data)
        print("Decryption Completed successfully !!")

    except Exception as e:
        print(f"Error: {e}. Please try again!")
if __name__=='__main__':
    main()

