from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password: str) -> str:
    return generate_password_hash(password, method='sha256')


def check_password(saved_password: str, entered_password: str) -> bool:
    return check_password_hash(saved_password, entered_password)
