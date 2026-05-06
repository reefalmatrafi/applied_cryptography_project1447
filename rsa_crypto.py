from rsa_keygen import e, d, n

def encrypt(message, e, n):
    cipher = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n)
        cipher.append(c)
    return cipher


def decrypt(cipher, d, n):
    message = ""
    for c in cipher:
        m = pow(c, d, n)
        message += chr(m)
    return message


# ================= Testing =================

messages = ["HELLO", "RSA TEST", "SECURITY"]

print("\n--- Encryption & Decryption Testing ---")

for message in messages:
    print("\nOriginal:", message)

    encrypted = encrypt(message, e, n)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, d, n)
    print("Decrypted:", decrypted)