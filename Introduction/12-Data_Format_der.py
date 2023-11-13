from Crypto.PublicKey import RSA
from Crypto.IO import PEM

# Leer el archivo .der
with open('.2048-rsa.der', 'rb') as f:
    der_data = f.read()

# Convertir a formato PEM
pem_data = PEM.encode(der_data, "RSA PUBLIC KEY")

# Importar la clave pública
public_key = RSA.importKey(pem_data)

# Obtener el módulo como un número decimal
n = public_key.n
print("[+] El modulo secreto de der -> pem es: ", n)
