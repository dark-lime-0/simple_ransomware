import os
from cryptography.fernet import Fernet

# write a decryption script of the ransomware
# created by Youssef/dark-lime-0

def main()->None:
    files=[]
    for file in os.listdir():
            if file == 'enc_file.py' or file =="thekey.key" or file == 'dec_file.py':
                    continue
            if os.path.isfile(file):
                    files.append(file)
    print(files)

    with open("thekey.key", 'rb') as thekey:    # save the decryption key in a variable
        key=thekey.read()

    for file in files :                         # encrypt the plaintext data
        with open(file,'rb') as thefile:
            containts = thefile.read()
        dec_data = Fernet(key).decrypt(containts)
        with open(file, 'wb') as thefile :
            thefile.write(dec_data)

    print("Decryption Completed successfully !!")

if __name__=='__main__':
    main()

