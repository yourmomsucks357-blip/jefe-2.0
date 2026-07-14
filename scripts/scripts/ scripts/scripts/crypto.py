from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    """Generate a Fernet key for symmetric encryption."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt a file using Fernet."""
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(f"{file_path}.enc", "wb") as f:
        f.write(encrypted)
    return f"File encrypted: {file_path}.enc"

def decrypt_file(encrypted_path, key):
    """Decrypt a file using Fernet."""
    fernet = Fernet(key)
    with open(encrypted_path, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    with open(encrypted_path.replace(".enc", ".dec"), "wb") as f:
        f.write(decrypted)
    return f"File decrypted: {encrypted_path.replace('.enc', '.dec')}"

if __name__ == "__main__":
    print("=== File Encryption Tool ===")
    key = generate_key()
    print(f"Key (save this!): {key.decode()}")

    file_path = input("Enter file to encrypt: ")
    print(encrypt_file(file_path, key))

    enc_file = input("Enter file to decrypt: ")
    print(decrypt_file(enc_file, key))
