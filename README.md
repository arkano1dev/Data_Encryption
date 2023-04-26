# Data_Encryption
## Introduction 
I made this code for know how to encrypt, decrypt and hash data maintening it secure and secret in the path of this information.

Consists of two Python modules: "Encryptor.py" and "UserApp.py". 

"Encryptor.py" contains functions for file encryption, decryption, password hashing, and data anonymization. 

"UserApp.py" uses these functions.

I use a dataset of the most common passwords only for *educational purpose*

## Requirements

For run this code you will need:

-Hashlib

-Os

-Cryptography

-Pandas

-Numpy

Make sure to install this correctly using the function *_pip install_* in the comand windows.

## Funtions

**encrypt_file(file_path, key):** 

Encrypts a file using Fernet encryption. 
Use two arguments: the path of the file to be encrypted and the encryption key. 
Reads the contents of the file, encrypts them using the provided key, and writes the encrypted contents back to the file.


**decrypt_file(file_path, key):** 

Decrypts an encrypted file. 
It takes two arguments: the path of the encrypted file and the encryption key. 
Reads the encrypted contents of the file, decrypts them using the provided key, and writes the decrypted contents back to the file.


**hash_password(password):** 

Hashes a given password using SHA-256. 
It need one argument, the password to be hashed. 
Encodes the password as UTF-8, hashes it using SHA-256, and returns the hashed password in hexadecimal format.


**anonymize_data(dataframe):**

Anonymizes a dataset by replacing identifiable data with random values. 
It takes one argument, a pandas dataframe. 
The function iterates over each column in the dataframe and checks if the column contains identifiable data (e.g. passwords or length of the password). 
If the column contains identifiable data, the function replaces the values in the column with randomly generated data.


In the UserApp.py file you can run these functions and:

Hash_password funtion selects a random password from the dataset hashes it and save a file with the selected random password and the corresponding hash.

To run the UserApp.py module, ensure that the Encryptor.py module is in the same directory as UserApp.py. 

Also, ensure that the sample dataset "common_passwords.csv" is in the same directory as UserApp.py. Run the UserApp.py module in a Python environment.

If you have any doubts do not hesitate to contact me, I´m happy to help you!

