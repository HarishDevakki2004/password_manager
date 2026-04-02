from cryptography.fernet import Fernet
import os

KEY_FILE = "data/key.key"


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key


def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()


def decrypt_password(token):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()