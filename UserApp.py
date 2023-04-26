import numpy as np
import csv
import random
from cryptography.fernet import Fernet
import pandas as pd
from Encryptor import encrypt_file, decrypt_file, hash_password, anonymize_data

file_path= "C://Programación//Data_Encryption//common_passwords.csv"

if __name__ == "__main__":
    # Encrypt a file 

    key = Fernet.generate_key()

    encrypt_file("common_passwords_For_Encrypt.csv", key)

    # Decrypt a file

    decrypt_file("common_passwords_For_Encrypt.csv", key)

    # Hash a random password using SHA-256
    # Load the CSV file into a dataframe

    df = pd.read_csv("common_passwords.csv")

    # Select a random row from the dataframe

    random_row = np.random.randint(len(df))

    # Access the password from the selected row

    password = df.loc[random_row, "password"]

    hashed_password = hash_password(password)

    # Save this hashed password in a hashed_password.txt 

    with open("hashed_password.txt", "w") as file:

    # Write the variable to the file

        file.write(f"The selected password is: {password}\nThe hashed password is: {hashed_password}")


    # Anonymize a dataset by replacing identifiable data with random values

    dataframe = pd.read_csv("common_passwords.csv")

    anonymized_dataframe = anonymize_data(dataframe)

    anonymized_dataframe.to_csv("anonymized.csv", index=False)
