from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key created.")

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print("Encrypted:", filename)

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)
    print("Decrypted:", filename)

if __name__ == "__main__":
    print("1) Create Key\n2) Encrypt File\n3) Decrypt File")
    choice = input("Choice: ")

    if choice == "1":
        create_key()
    elif choice == "2":
        encrypt_file(input("File: "))
    elif choice == "3":
        decrypt_file(input("Encrypted file: "))
