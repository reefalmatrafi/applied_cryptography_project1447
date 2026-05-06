from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# =========================================================
# RSA FUNCTIONS (Used to protect AES key)
# =========================================================

def gcd(a, b):
    """Calculate Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    """Compute d such that (e * d) mod phi = 1"""

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1

        gcd_value, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1

        return gcd_value, x, y

    gcd_value, x, _ = extended_gcd(e, phi)

    if gcd_value != 1:
        raise ValueError("e and phi are not coprime.")

    return x % phi


def rsa_encrypt_number(m, e, n):
    """Encrypt a number using RSA: C = m^e mod n"""
    return pow(m, e, n)


def rsa_decrypt_number(c, d, n):
    """Decrypt a number using RSA: m = c^d mod n"""
    return pow(c, d, n)


# =========================================================
# AES FUNCTIONS (Used to encrypt actual message)
# =========================================================

def aes_encrypt(message, key):
    """
    Encrypt message using AES (CBC mode)
    - IV adds randomness
    - Padding ensures block size = 16 bytes
    """
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv, ciphertext


def aes_decrypt(ciphertext, key, iv):
    """Decrypt AES message"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext.decode()


# =========================================================
# MAIN PROGRAM
# =========================================================

print("=" * 60)
print("HYBRID RSA + AES ENCRYPTION DEMO")
print("=" * 60)

# -----------------------------
# Step 1: RSA Key Generation
# -----------------------------

p = 53
q = 61

n = p * q
phi = (p - 1) * (q - 1)

e = 17  # public exponent
d = mod_inverse(e, phi)  # private exponent

print("\n[RSA KEY GENERATION]")
print(f"p = {p}, q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"Public Key (e, n) = ({e}, {n})")
print(f"Private Key (d, n) = ({d}, {n})")

# -----------------------------
# Step 2: Original Message
# -----------------------------

message = "Hybrid encryption protects data!"

print("\n[ORIGINAL MESSAGE]")
print(message)

# -----------------------------
# Step 3: Generate AES Key
# -----------------------------

aes_key = get_random_bytes(16)  # 128-bit key

print("\n[AES KEY]")
print(aes_key.hex())

# -----------------------------
# Step 4: Encrypt Message using AES
# -----------------------------

iv, encrypted_msg = aes_encrypt(message, aes_key)

print("\n[AES ENCRYPTION]")
print("IV:", iv.hex())
print("Ciphertext:", encrypted_msg.hex())

# -----------------------------
# Step 5: Encrypt AES Key using RSA
# -----------------------------

encrypted_key = []

# RSA cannot encrypt full AES key directly → encrypt byte by byte
for byte in aes_key:
    encrypted_key.append(rsa_encrypt_number(byte, e, n))

print("\n[RSA ENCRYPTION OF AES KEY]")
print(encrypted_key)

# -----------------------------
# Step 6: Decrypt AES Key using RSA
# -----------------------------

decrypted_key_bytes = []

for enc_byte in encrypted_key:
    decrypted_key_bytes.append(rsa_decrypt_number(enc_byte, d, n))

decrypted_key = bytes(decrypted_key_bytes)

print("\n[RSA DECRYPTION OF AES KEY]")
print(decrypted_key.hex())

# -----------------------------
# Step 7: Decrypt Message using AES
# -----------------------------

decrypted_msg = aes_decrypt(encrypted_msg, decrypted_key, iv)

print("\n[AES DECRYPTION]")
print(decrypted_msg)

# -----------------------------
# Step 8: Verification
# -----------------------------

print("\n[VERIFICATION]")
print("AES Key Match:", aes_key == decrypted_key)
print("Message Match:", message == decrypted_msg)

# -----------------------------
# Security Explanation
# -----------------------------

print("\n[SECURITY INSIGHT]")
print("AES encrypts the actual data (fast and secure).")
print("RSA protects the AES key.")
print("Even if RSA is weak, attacker still needs AES key to decrypt message.")