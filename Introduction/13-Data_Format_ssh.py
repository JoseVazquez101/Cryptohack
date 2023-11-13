from Crypto.PublicKey import RSA

f = open('.bruce_rsa.pub', 'r')
pubkey = RSA.import_key(f.read())

print("[+] EL modulo n de la clave RSA es: ", pubkey.n)
