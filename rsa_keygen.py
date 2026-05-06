import random
from weak_prng import WeakPRNG


class RSAKeyGenerator:
    """
    RSA Key Generator with weak random number generation.
    This is for demonstration purposes only.
    """

    def __init__(self, p, q, seed=None):
        self.p = p
        self.q = q
        self.prng = WeakPRNG(seed=seed)
        self.keys = {}
        self.n = None
        self.phi = None

    def generate_keys(self):
        self.n = self.p * self.q
        print(f"[*] n = p × q = {self.p} × {self.q} = {self.n}")

        self.phi = (self.p - 1) * (self.q - 1)
        print(f"[*] φ(n) = (p-1)(q-1) = {self.p - 1} × {self.q - 1} = {self.phi}")

        e_candidates = [3, 5, 17, 65537]
        e = self.choose_valid_e(e_candidates)
        print(f"[*] e (public exponent) = {e}")

        d = self.mod_inverse(e, self.phi)
        print(f"[*] d (private exponent) = {d}")

        verification = (e * d) % self.phi
        print(f"[✓] Verification: (e × d) mod φ(n) = {verification} (should be 1)")

        self.keys = {
            "public_key": {"e": e, "n": self.n},
            "private_key": {"d": d, "n": self.n},
            "p": self.p,
            "q": self.q,
            "phi": self.phi
        }

        return self.keys

    def choose_valid_e(self, candidates):
        """
        Choose e using weak randomness, but make sure it is valid for RSA.
        e must be coprime with phi(n).
        """
        random.shuffle(candidates)

        for e in candidates:
            if self.gcd(e, self.phi) == 1:
                return e

        raise ValueError("No valid e found.")

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mod_inverse(self, e, phi):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1

            gcd_value, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1

            return gcd_value, x, y

        gcd_value, x, _ = extended_gcd(e, phi)

        if gcd_value != 1:
            raise ValueError("e and phi(n) are not coprime.")

        return x % phi

    def get_public_key(self):
        return self.keys["public_key"]

    def get_private_key(self):
        return self.keys["private_key"]

    def display_keys(self):
        print("\n" + "=" * 60)
        print("RSA KEY GENERATION COMPLETE")
        print("=" * 60)

        print("\n[PUBLIC KEY]")
        print(f"  e = {self.keys['public_key']['e']}")
        print(f"  n = {self.keys['public_key']['n']}")

        print("\n[PRIVATE KEY]")
        print(f"  d = {self.keys['private_key']['d']}")
        print(f"  n = {self.keys['private_key']['n']}")

        print("\n[ADDITIONAL INFO]")
        print(f"  p = {self.p}")
        print(f"  q = {self.q}")
        print(f"  φ(n) = {self.phi}")

        print("=" * 60 + "\n")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("RSA KEY GENERATOR WITH WEAK PRNG")
    print("=" * 60 + "\n")

    keygen = RSAKeyGenerator(p=53, q=61, seed=42)
    keygen.generate_keys()
    keygen.display_keys()

    print("[!] WARNING: This demonstrates WEAK key generation.")
    print("[!] With weak randomness, RSA key generation may become predictable.")
