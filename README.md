# applied_cryptography_project1447

weak_prng.py Weak Random Number Generator.
This version intentionally creates predictable values to demonstrate vulnerability.

rsa_prng.py RSA Key Generator with weak random number generation.
This is for demonstration purposes only.

ai_key_predictor.py AI Integration: This model learns patterns from a weak random number generator
and tries to predict the next RSA key component.

hybird_rsa_aes.py This code demonstrates Hybrid Encryption using both AES and RSA algorithms.
AES is used to encrypt the actual message quickly and securely, while RSA is used to protect the AES key.
Finally, the program decrypts the AES key and message, then verifies that the original data is recovered correctly.
