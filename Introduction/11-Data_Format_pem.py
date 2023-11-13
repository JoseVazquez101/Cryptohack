from Crypto.PublicKey import RSA

# Leer la clave del archivo
with open(".key_mail.pem", "rb") as key_file:
    key_data = key_file.read()

# Importar la clave
key = RSA.importKey(key_data)

# Obtener el exponente privado d como un entero
d = key.d

print("[+] Clave privada d:", d)
