from cryptography.fernet import Fernet


def aes_encrypt(string_: str, key: bytes) -> bytes:
    f = Fernet(key)
    encrypted_string = f.encrypt(string_.encode())
    return encrypted_string


def aes_decrypt(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    decrypted_string = f.decrypt(token)
    return decrypted_string.decode()
