import random
from math import 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=50, end=200):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    
    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

public_key, private_key = generate_keys()

print("Public Key:", public_key)
print("Private Key:", private_key)

message = input("Masukkan pesan: ")

encrypted = encrypt(public_key, message)
print("Pesan terenkripsi:", encrypted)

decrypted = decrypt(private_key, encrypted)
print("Pesan terdekripsi:", decrypted)
