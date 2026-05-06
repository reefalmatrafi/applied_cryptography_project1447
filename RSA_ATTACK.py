import time
import math

"""
RSA Brute Force Attack Implementation
======================================
This module implements a brute force attack on RSA encryption
by factorizing the modulus n using trial division.

Author: Reem Alfahmi
Date: 2026-04-30
Purpose: Educational - Demonstrate RSA vulnerability with small primes
"""

class RSABruteForceAttack:
    """
    A class to perform brute force attacks on RSA encryption.
    
    Attributes:
        n (int): RSA modulus
        e (int): RSA public exponent
        cipher_list (list): Encrypted message as list of integers
    """
    
    def __init__(self, n, e, cipher_list):
        """
        Initialize the attack parameters.
        
        Args:
            n (int): RSA modulus (product of two primes p and q)
            e (int): Public exponent
            cipher_list (list): Ciphertext as list of encrypted values
        """
        self.n = n
        self.e = e
        self.cipher_list = cipher_list
        self.p = None
        self.q = None
        self.phi = None
        self.d = None
        self.attack_time = 0
    
    def factorize(self):
        """
        Factorize n using trial division (brute force).
        
        Time Complexity: O(√n)
        Space Complexity: O(1)
        
        Returns:
            tuple: (p, q, time_taken) or (None, None, 0) if factorization fails
        """
        print("[*] Starting factorization of n using trial division...")
        start_time = time.perf_counter()
        
        # Trial division: test all integers from 2 to sqrt(n)
        sqrt_n = int(math.sqrt(self.n))
        
        for i in range(2, sqrt_n + 1):
            if self.n % i == 0:
                p = i
                q = self.n // i
                
                end_time = time.perf_counter()
                factor_time = end_time - start_time
                
                print(f"[+] Found p = {p}, q = {q}")
                print(f"[+] Verification: {p} x {q} = {p * q}")
                print(f"[+] Factorization completed in {factor_time:.8f} seconds")
                
                return p, q, factor_time
        
        print("[-] Factorization failed: n could not be factorized")
        return None, None, 0
    
    def compute_phi(self):
        """
        Compute Euler's totient function phi(n) = (p-1)(q-1).
        
        Returns:
            int: phi(n)
        """
        if self.p is None or self.q is None:
            raise ValueError("p and q must be set before computing phi(n)")
        
        self.phi = (self.p - 1) * (self.q - 1)
        print(f"[+] Computed phi(n) = ({self.p}-1) x ({self.q}-1) = {self.phi}")
        return self.phi
    
    def compute_private_key(self):
        """
        Compute the private key d using modular inverse.
        
        Finds d such that: (e x d) ≡ 1 (mod phi(n))
        Uses Python's built-in pow(e, -1, phi) function.
        
        Returns:
            int: Private exponent d
        """
        if self.phi is None:
            raise ValueError("phi(n) must be computed before finding d")
        
        try:
            self.d = pow(self.e, -1, self.phi)
            print(f"[+] Computed private key d = {self.d}")
            print(f"[+] Verification: ({self.e} x {self.d}) mod {self.phi} = {(self.e * self.d) % self.phi}")
            return self.d
        except ValueError:
            print("[-] Error: Cannot compute modular inverse (gcd(e, phi) != 1)")
            return None
    
    def decrypt_message(self):
        """
        Decrypt the ciphertext using the recovered private key.
        
        For each ciphertext character c:
        plaintext m = c^d mod n
        
        Returns:
            str: Decrypted message
        """
        if self.d is None:
            raise ValueError("Private key d must be computed before decryption")
        
        decrypted_message = ""
        
        for c in self.cipher_list:
            # Compute m = c^d mod n using fast modular exponentiation
            m = pow(c, self.d, self.n)
            decrypted_message += chr(m)
        
        print(f"[+] Decrypted message: '{decrypted_message}'")
        return decrypted_message
    
    def execute_attack(self):
        """
        Execute the complete brute force attack.
        
        Steps:
        1. Factorize n to find p and q
        2. Compute phi(n)
        3. Compute private key d
        4. Decrypt the message
        
        Returns:
            dict: Attack results containing p, q, d, and decrypted message
        """
        print("\n" + "="*70)
        print("RSA BRUTE FORCE ATTACK")
        print("="*70)
        
        print(f"\n[*] Attack Parameters:")
        print(f"    - Public Key (e, n): ({self.e}, {self.n})")
        print(f"    - Ciphertext: {self.cipher_list}")
        
        # Start total attack timer
        total_start = time.perf_counter()
        
        # Step 1: Factorization
        print(f"\n[Step 1] Factorizing n")
        print("-" * 70)
        self.p, self.q, factor_time = self.factorize()
        
        if self.p is None:
            print("\n[-] Attack failed: Unable to factorize n")
            return None
        
        # Step 2: Compute phi(n)
        print(f"\n[Step 2] Computing phi(n)")
        print("-" * 70)
        self.compute_phi()
        
        # Step 3: Compute private key
        print(f"\n[Step 3] Computing private key d")
        print("-" * 70)
        if self.compute_private_key() is None:
            print("\n[-] Attack failed: Unable to compute private key")
            return None
        
        # Step 4: Decrypt message
        print(f"\n[Step 4] Decrypting message")
        print("-" * 70)
        decrypted_message = self.decrypt_message()
        
        # End total attack timer
        total_end = time.perf_counter()
        self.attack_time = total_end - total_start
        
        # Print results
        print(f"\n" + "="*70)
        print("ATTACK SUCCESSFUL")
        print("="*70)
        print(f"[+] Recovered p = {self.p}")
        print(f"[+] Recovered q = {self.q}")
        print(f"[+] Recovered d = {self.d}")
        print(f"[+] Decrypted message = '{decrypted_message}'")
        print(f"[+] Total attack time = {self.attack_time:.8f} seconds")
        print("="*70 + "\n")
        
        return {
            'p': self.p,
            'q': self.q,
            'd': self.d,
            'message': decrypted_message,
            'time': self.attack_time
        }


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def encrypt_message(message, e, n):
    """
    Encrypt a message using RSA public key.
    
    Args:
        message (str): Plaintext message
        e (int): Public exponent
        n (int): RSA modulus
    
    Returns:
        list: List of encrypted character values
    """
    cipher = []
    for char in message:
        m = ord(char)  # Convert character to ASCII value
        c = pow(m, e, n)  # Compute c = m^e mod n
        cipher.append(c)
    return cipher


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("RSA BRUTE FORCE ATTACK - DEMONSTRATION")
    print("="*70 + "\n")
    
    # RSA Parameters
    n = 3233
    e = 17
    
    # Test message
    test_message = "HELLO"
    
    # Step 1: Encrypt the message
    print(f"[*] Encrypting message: '{test_message}'")
    cipher = encrypt_message(test_message, e, n)
    print(f"[+] Ciphertext: {cipher}\n")
    
    # Step 2: Execute brute force attack
    attack = RSABruteForceAttack(n, e, cipher)
    result = attack.execute_attack()
    
    # Step 3: Verify results
    if result:
        print("[*] Verification:")
        print(f"[+] Original message: '{test_message}'")
        print(f"[+] Recovered message: '{result['message']}'")
        print(f"[+] Match: {test_message == result['message']}\n")
        
        # Display vulnerability assessment
        print("="*70)
        print("VULNERABILITY ASSESSMENT")
        print("="*70)
        print(f"""
With small primes (p={result['p']}, q={result['q']}):
    - RSA Modulus n = {n}
    - sqrt(n) ~ {int(math.sqrt(n))}
    - Attack Complexity: O(sqrt(n)) ~ {int(math.sqrt(n))} iterations
    - Actual Time: {result['time']:.8f} seconds
    - SECURITY LEVEL: BROKEN

With 1024-bit primes (recommended):
    - RSA Modulus n ~ 2^2048
    - sqrt(n) ~ 2^1024 ~ 10^308
    - Attack Time: ~10^100 years
    - SECURITY LEVEL: SECURE

CONCLUSION:
RSA security depends on the difficulty of factorizing large numbers.
Small primes make RSA completely insecure.
""")
        print("="*70)