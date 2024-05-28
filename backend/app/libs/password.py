"""Password encryption and decryption"""
import bcrypt
import base64


def hash_password(plain_text_password: str) -> str:
    """Encrypt"""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return base64.b64encode(hashed_password).decode('utf-8')


def password_checked(plain_text_password: str, hashed_password: bytes) -> bool:
    """Check encrypt"""
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)
