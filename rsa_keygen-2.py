# RSA key generation
# chosen 2 primes 
q=61 
p=53
# caculate n and phi
n= q * p
phi =(p-1) * (q-1)
# chosen e with the conditions
e = 17 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if gcd(e, phi) == 1:
    print("e is valid")
else:
    print("choose another e")


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
        
d = mod_inverse(e, phi)

print("public key:", (e, n))
print("privet key:", (d, n))

