import hashlib
import os

MASTER_FILE = "data/master.hash"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_master_password(password):
    hashed = hash_password(password)
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)


def verify_master_password(password):
    if not os.path.exists(MASTER_FILE):
        setup_master_password(password)
        return True

    with open(MASTER_FILE, "r") as f:
        stored_hash = f.read()

    return stored_hash == hash_password(password)