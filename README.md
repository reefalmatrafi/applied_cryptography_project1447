# applied_cryptography_project1447
weak_prng.py 
Weak Random Number Generator.
This version intentionally creates predictable values to demonstrate vulnerability.

rsa_keygen.py 
This code generates RSA public and private keys using a weak random number generator (PRNG).
It calculates n, ϕ(n), selects a valid public exponent e, and computes the private key d.
The program demonstrates that weak randomness can make RSA key generation predictable and reduce security.

rsa_prng.py 
RSA Key Generator with weak random number generation.
This is for demonstration purposes only.

ai_key_predictor.py 
AI Integration: This model learns patterns from a weak random number generator
and tries to predict the next RSA key component.

hybird_rsa_aes.py 
This code demonstrates Hybrid Encryption using both AES and RSA algorithms.
AES is used to encrypt the actual message quickly and securely, while RSA is used to protect the AES key.
Finally, the program decrypts the AES key and message, then verifies that the original data is recovered correctly.

attack.py 
This code demonstrates a brute-force attack on RSA encryption by factorizing the public modulus n to recover the prime numbers p and q. After that, it calculates φ(n), reconstructs the private key d, and decrypts the encrypted message. The program shows that RSA with small key sizes is insecure and can be broken quickly. 

complexity_analysis.py 
This code tests a brute-force attack on small RSA keys by trying to factor n into p and q.
It measures the average time needed to recover the prime numbers for different key sizes.
Finally, it prints a summary table and draws a graph showing that larger RSA keys take longer to break.


RSA Digital Mailbox (HTML Interface)
This code implements a secure digital mailbox simulation using HTML, CSS, and JavaScript. The system allows a sender to write and encrypt messages using RSA encryption before transmission. The encrypted ciphertext is displayed during transmission, while the receiver can decrypt the message using the private key. The interface visually demonstrates RSA key generation, encryption, decryption, and secure communication in an interactive way.
