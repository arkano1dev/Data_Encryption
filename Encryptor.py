import hashlib
import os
from cryptography.fernet import Fernet
import pandas as pd

file_path= "C://Programación//Data_Encryption//common_passwords.csv"

# Define a function to encrypt a file using Fernet encryption
def encrypt_file(file_path, key):
    # Generate a Fernet key from the provided key
    fernet_key = Fernet(key)

    # Read the contents of the file into memory
    with open(file_path, "rb") as file:
        file_contents = file.read()

    # Encrypt the file contents using Fernet encryption
    encrypted_contents = fernet_key.encrypt(file_contents)

    # Write the encrypted contents back to the file
    with open(file_path, "wb") as file:
        file.write(encrypted_contents)


# Define a function to decrypt a file using Fernet encryption
def decrypt_file(file_path, key):
    # Generate a Fernet key from the provided key
    fernet_key = Fernet(key)

    # Read the encrypted contents of the file into memory
    with open(file_path, "rb") as file:
        encrypted_contents = file.read()

    # Decrypt the file contents using Fernet encryption
    decrypted_contents = fernet_key.decrypt(encrypted_contents)

    # Write the decrypted contents back to the file
    with open(file_path, "wb") as file:
        file.write(decrypted_contents)


# Define a function to hash a password using SHA-256
def hash_password(password):
    # Encode the password as UTF-8
    password_bytes = password.encode("utf-8")

    # Hash the password using SHA-256
    hashed_bytes = hashlib.sha256(password_bytes).digest()

    # Convert the hashed bytes to a hex string representation
    hashed_string = hashed_bytes.hex()

    return hashed_string


# Define a function to anonymize a dataset by replacing identifiable data with random values
def anonymize_data(dataframe):
    # Iterate over each column in the dataframe
    for column in dataframe.columns:
        # Check if the column contains identifiable data (e.g. passwords, length of the password)
        if "password" in column.lower() or "length" in column.lower():
            # Replace the values in the column with randomly generated data
            dataframe[column] = [os.urandom(10).hex() for _ in range(len(dataframe))]

    return dataframe


# Example usage of the functions defined above
if __name__ == "__main__":
    # Encrypt a file using Fernet encryption
    key = Fernet.generate_key()
    encrypt_file("common_passwords.csv", key)

    # Decrypt a file using Fernet encryption
    decrypt_file("common_passwords.csv", key)

    # Hash a password using SHA-256
    password = "password123"
    hashed_password = hash_password(password)

    # Save this hashed password in a file.txt 
    with open("hashed_password.txt", "w") as file:
    # Write the variable to the file
        file.write(hashed_password)


    # Anonymize a dataset by replacing identifiable data with random values
    dataframe = pd.read_csv("common_passwords.csv")
    anonymized_dataframe = anonymize_data(dataframe)
    anonymized_dataframe.to_csv("anonymized.csv", index=False)
