from Crypto.PublicKey import RSA

with open('transparency.pem', 'r') as f:
    pubkey = RSA.import_key(f.read())

print("\n[+] EL modulo n de la clave RSA es: ", pubkey.n)
print("\n[+] Formato HEX -> ",hex(pubkey.n))
