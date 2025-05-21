def short_key_cipher(key, message):
    """
    Encrypts a message using a short key cipher.

    Args:
        key: The encryption key (a string).
        message: The message to encrypt (a string).

    Returns:
        The encrypted message (a string).
    """

    key_length = len(key)
    encrypted_message = ""

    for i, char in enumerate(message):
        key_char = key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char)) 
        encrypted_message += encrypted_char

    return encrypted_message

key = "mysecretkey"
message = "Camilo+**1057575431"
encrypted_message = short_key_cipher(key, message)
print("Encrypted:", encrypted_message)
