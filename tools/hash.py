import hashlib


def hash_password(password: str) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    return hash_object.hexdigest()
