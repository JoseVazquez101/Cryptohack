from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

p = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
g = "0x02"

#Transformar p y g a entero
Primo = int(p, 16)
Base = int(g, 16)

#Interceptamos Alice y lo hacemos entero
A=str(input("\nIntercepted from Alice (A): "))
A_int=int(A, 16)

#Creo mi propio numero exponente que yo conozco
mynum=int(input("\nTu numero exponente: "))

#Creo una nueva A y su Json
new_A=pow(Base, mynum, Primo)
new_A_hex=hex(new_A)
print("\nJSON Alice:\n{\"p\": \""+p+"\", \"g\": \"0x02\", \"A\": \""+new_A_hex+"\"}\n")

#Intercepto Bob y lo hago entero
B=str(input("\nIntercepted from Bob: "))
B_int=int(B, 16)

#Creo una nueva B y la mando, con el mismo exponente que creé al inicio
new_B=pow(Base, mynum, Primo)
new_B_hex=hex(new_B)
print("\nJSON Bob:\n{\"B\": \""+new_B_hex+"\"}")

#Como Alice es quien me manda iv y flag, creo una llave la cual es en si (a es un numero que no conocemos):
keyA=pow(A_int, mynum, Primo) # = (g^a%p) ^ mynum % p | mynum es por el exponente que utilicé para crear la nueva B

secret=keyA

iv = str(input("\niv response: "))
ciphertext = str(input("ciphertext: "))

# Derive AES key from shared secret
sha1 = hashlib.sha1()
sha1.update(str(secret).encode('ascii'))
key = sha1.digest()[:16]
# Encrypt flag
cipher_hex = bytes.fromhex(ciphertext)
iv = bytes.fromhex(iv)
cipher = AES.new(key, AES.MODE_CBC, iv)
# Prepare data to send
flag = cipher.decrypt(cipher_hex)
print("\n\nFlag: ", flag)


