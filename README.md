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

rsa_crypto.py This code implements basic RSA encryption and decryption for text messages.
Each character is converted into a number, encrypted using the RSA public key, then decrypted using the private key to recover the original message.The program tests the process on multiple messages to verify that encryption and decryption work correctly.

rsa_keygen-2.py This code generates RSA public and private keys using two prime numbers.
It calculates n and ϕ(n), checks that the public exponent e is valid, then computes the private key d.
Finally, the program prints the public key and private key used for RSA encryption and decryption.

RSA_ATTACK.py This code demonstrates a brute-force attack on RSA by factorizing the public modulus n to recover p and q.
After finding the primes, it calculates ϕ(n), recovers the private key d, and decrypts the message.
The program shows that RSA with small prime numbers is insecure and can be broken quickly.

complexity_analysis.py This code tests a brute-force attack on small RSA keys by trying to factor n into p and q.
It measures the average time needed to recover the prime numbers for different key sizes.
Finally, it prints a summary table and draws a graph showing that larger RSA keys take longer to break.

rsa_keygen.py This code generates RSA keys using fixed prime numbers and a weak random generator.
It calculates n, ϕ(n), chooses a valid public exponent e, and computes the private key d.
The main idea is to show that weak randomness can make RSA key generation predictable and less secure.
