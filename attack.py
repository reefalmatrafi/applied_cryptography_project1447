"""
RSA BRUTE FORCE ATTACK - MODIFIED VERSION
==========================================
Performs prime factorization on a small n to derive p and q,
then computes the private key d.

Author: Reem Alfahmi (Updated)
Purpose: Educational - Demonstrates RSA vulnerability with small primes
"""

import time
import math

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """
    Compute modular inverse d such that (e * d) % phi = 1
    Uses Extended Euclidean Algorithm (not built-in pow)
    """
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"e ({e}) and phi ({phi}) are not coprime")
    return x % phi

def factorize_bruteforce(n):
    """
    Factorize n using trial division.
    Returns p, q, and time taken.
    """
    print(f"[*] Attempting to factorize n = {n}")
    start_time = time.time()
    
    # Only need to check up to sqrt(n)
    limit = int(math.isqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            p = i
            q = n // i
            elapsed = time.time() - start_time
            print(f"[+] Found factors in {elapsed:.6f} seconds!")
            print(f"    p = {p}")
            print(f"    q = {q}")
            print(f"    Verification: {p} × {q} = {p * q} ✓")
            return p, q, elapsed
    
    print("[-] Failed to factorize n!")
    return None, None, None

def compute_phi(p, q):
    """Compute Euler's totient φ(n) = (p-1)(q-1)"""
    phi = (p - 1) * (q - 1)
    print(f"[+] φ(n) = ({p}-1) × ({q}-1) = {phi}")
    return phi

def compute_private_key(e, phi):
    """Compute private exponent d using modular inverse"""
    d = mod_inverse(e, phi)
    print(f"[+] Private key d = {d}")
    print(f"[+] Verification: ({e} × {d}) mod {phi} = {(e * d) % phi} ✓")
    return d

def decrypt_message(cipher_list, d, n):
    """
    Decrypt ciphertext using recovered private key.
    For each c: m = c^d mod n
    """
    decrypted = ""
    for c in cipher_list:
        m = pow(c, d, n)  # Fast modular exponentiation
        decrypted += chr(m)
    return decrypted

def encrypt_message(message, e, n):
    """Helper function to encrypt a message for testing"""
    cipher = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n)
        cipher.append(c)
    return cipher


class RSABruteForceAttack:
    """
    Complete RSA Brute Force Attack Class
    """
    
    def __init__(self, n, e, cipher_list=None):
        self.n = n
        self.e = e
        self.cipher_list = cipher_list
        self.p = None
        self.q = None
        self.phi = None
        self.d = None
        self.attack_time = 0
    
    def execute_attack(self):
        """Execute the full attack sequence"""
        print("\n" + "="*60)
        print("    RSA BRUTE FORCE ATTACK")
        print("="*60)
        print(f"\n[Target]")
        print(f"   Public Key (e, n): ({self.e}, {self.n})")
        
        if self.cipher_list:
            print(f"   Ciphertext length: {len(self.cipher_list)} blocks")
        
        # Start timer
        start_time = time.time()
        
        # Step 1: Factorize n
        print(f"\n[Step 1] Factorizing n")
        print("-"*40)
        self.p, self.q, _ = factorize_bruteforce(self.n)
        
        if self.p is None:
            print("\n[-] Attack failed: Cannot factorize n")
            return None
        
        # Step 2: Compute φ(n)
        print(f"\n[Step 2] Computing φ(n)")
        print("-"*40)
        self.phi = compute_phi(self.p, self.q)
        
        # Step 3: Compute private key d
        print(f"\n[Step 3] Computing private key d")
        print("-"*40)
        self.d = compute_private_key(self.e, self.phi)
        
        # Step 4: Decrypt if ciphertext provided
        decrypted_message = None
        if self.cipher_list:
            print(f"\n[Step 4] Decrypting message")
            print("-"*40)
            decrypted_message = decrypt_message(self.cipher_list, self.d, self.n)
            print(f"[+] Decrypted message: '{decrypted_message}'")
        
        # End timer
        self.attack_time = time.time() - start_time
        
        # Results
        print("\n" + "="*60)
        print("    ATTACK RESULTS")
        print("="*60)
        print(f"✓ Recovered p = {self.p}")
        print(f"✓ Recovered q = {self.q}")
        print(f"✓ Recovered d (Private Key) = {self.d}")
        if decrypted_message:
            print(f"✓ Decrypted message = '{decrypted_message}'")
        print(f"✓ Total attack time = {self.attack_time:.6f} seconds")
        print("="*60)
        
        # Security warning
        print("\n" + "!"*60)
        print("  VULNERABILITY DEMONSTRATED!")
        print(f"  n = {self.n} was factorized in {self.attack_time:.6f} seconds.")
        print("  Small RSA keys are completely insecure!")
        print("  Real systems must use n ≥ 2048 bits (≈ 617 digits).")
        print("!"*60)
        
        return {
            'p': self.p,
            'q': self.q,
            'd': self.d,
            'phi': self.phi,
            'message': decrypted_message,
            'time': self.attack_time
        }


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Example 1: Attack RSA with known small n (from your project)
    print("\n" + "="*60)
    print("  EXAMPLE 1: Attacking RSA with n = 3233")
    print("="*60)
    
    # RSA parameters (small primes: p=53, q=61)
    n = 3233
    e = 17
    
    # Test message encryption
    test_message = "A"
    cipher = encrypt_message(test_message, e, n)
    print(f"\n[*] Test message: '{test_message}'")
    print(f"[*] Encrypted to: {cipher}")
    
    # Execute attack
    attack = RSABruteForceAttack(n, e, cipher)
    result = attack.execute_attack()
    
    # Verify
    if result and result['message'] == test_message:
        print(f"\n[✓] VERIFICATION PASSED: Original message restored!")
    
    # Example 2: You can also test with n from your HTML mailbox
    print("\n" + "="*60)
    print("  EXAMPLE 2: How to use with your RSA Mailbox")
    print("="*60)
    print("""
    To use this attack on your rsa_mailbox.html:
    
    1. Open your browser console (F12)
    2. Get the current n and ciphertext
    3. Or manually enter them:
    
    from bruteforce_attack_final import RSABruteForceAttack
    
    n = 3233  # from your keys panel
    e = 17
    cipher = [2790, 1250, ...]  # from your cipher panel
    
    attack = RSABruteForceAttack(n, e, cipher)
    result = attack.execute_attack()
    
    print(f"Recovered private key d = {result['d']}")
    """)
