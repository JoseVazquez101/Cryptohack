#!/bin/bash

function ctrl_c() {
  echo -e "${red}\n\n[!] Saliendo...\n${normal}"
  rm $py_file 2>/dev/null
  rm out.txt 2>/dev/null
  exit 1
}
# Ctrl+c
trap ctrl_c INT

# Banner Mamón xd
red='\033[1;31m'
gray='\033[1;30m'
normal='\033[0m'
dark_yellow='\033[1;38;5;214m'
blue='\033[1;34m'

echo
echo -ne "${gray}╭╮${normal}                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n" && sleep 0.2
echo -ne "${gray}┃┃${normal}         ${red}     ⣴⠟⠛⠛⠛⠛⠛⠛⠛⠛⢛⣛⣻⣦⠀⠀⠀⠀⠀⠀⠀${normal}⠀\n"   && sleep 0.2
echo -ne "${gray}┃┃╱╱╭━━┳━━╮${normal}${red} ⠀⠀⠀⣿⣶⣶⡶⠀⠀⠛⠛⠋⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀${normal}\n"  && sleep 0.2
echo -ne "${gray}┃┃╱╭┫╭╮┃╭╮ ${normal}${red} ⠀⠀⠀⠘⠿⢿⡿⠿⠿⠿⠿⠿⠿⠿⠿⢿⡿⠀⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${gray}┃╰━╯┃╰╯┃╰╯┃${normal}${red} ⠀⠀⣠⣶⠿⠃⠀⠀⠀⠀⠀⠀  ⣶⡀⠘⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${gray}╰━━━┻━━┻━╮┃${normal}${red}⠀⣼⡟⠁⠀⠀⠀⠀⠀⠀⠀  ⠀ ⠉⠻⢷⣄⠈⢻⣧⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${gray}╱╱╱╱╱╱╱╭━╯┃${normal}${red}⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀ ⠀⣿⠀ ⢸⣿⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${gray}╱╱╱╱╱╱╱╰━━╯${normal}${red} ⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀  ⠀⣿ ⢸⣿⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${red}⠀⠀      ⠀⠀⠀⣿⠀    █ ▄▀█ █▀▄▀█  ⣿⠀ ⢸⣿⠀⠀⠀⠀⠀⠀  ${normal}\n" && sleep 0.2
echo -ne "${red}⠀         ⠀⠀⣿⡇⠀█▄█ █▀█ █░▀░█⠀⠀⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${red}⠀⠀         ⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${red}⠀       ⠀  ⠀⣿⡇⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀  ⠀⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${red}⠀       ⠀  ⠀⢻⣇⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀  ⠀⠟⠀⣸⡟⠀⠀⠀⠀⠀⠀${normal}\n" && sleep 0.2
echo -ne "${red}⠀⠀      ⠀⠀   ⠛⢷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡾⠛${normal}\n" && sleep 0.2
echo -ne "\n\n"

py_file=LogJam.py
target="socket.cryptohack.org"
port="13379"

echo -ne "${blue}[+]${normal} ${dark_yellow}Estableciendo conexión a${normal} ${blue}${target}:${port}${normal}\n"
echo
tempfile=$(mktemp)
{
  echo -ne '{"supported": ["DH64"]}\n';
  sleep 2;
  echo -ne '{"chosen": "DH64"}\n';
  sleep 2;
} | nc $target $port>$tempfile &
nc_pid=$!
received_data=false
wait $nc_pid

> out.txt

while read -r line; do
  echo "$line" | tee -a out.txt
  if [[ "$line" == *'"encrypted_flag"'* ]]; then
    received_data=true
    break
  fi
done <$tempfile

rm $tempfile

if $received_data; then
  echo -ne "\n${blue}[+]${normal} ${dark_yellow}Comunicación terminada${normal}\n" | tee -a out.txt
else
  echo "${red}[!] No se recibieron datos${normal}\n"
  exit 1
fi

#Valores

A=$(cat out.txt | grep -o '"A": "0x[^"]*' | cut -d'"' -f4)
iv=$(cat out.txt | grep -o '"iv": "[^"]*' | awk -F ': ' '{print $2}' | tr -d '"')
encrypted_flag=$(cat out.txt | grep -o '"encrypted_flag": "[^"]*' | awk -F ': ' '{print $2}' | tr -d '"')
B=$(cat out.txt | grep -o '"B": "0x[^"]*' | cut -d'"' -f4)
p=$(cat out.txt | grep -o '"p": "0x[^"]*' | cut -d'"' -f4)

############### PyLoad xd #############################3

py_load=$(cat << EOL

from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib
from sympy.ntheory import discrete_log
import pwn

# Convert bytes to int
p = "$p"
g = 2
A = "$A"
B = "$B"

# Convert hex to int
iv =  "$iv"
encrypted_flag = "$encrypted_flag"

# Values Converted
p = int(p, 16)
A = int(A, 16)
B = int(B, 16)
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)

# Base
print("\nBase (g): ", g)
# Power
print("Power (A): ", A)
# Modulus
print("Modulus (P): ", p)


def decrypt(secret, iv, cipher):
    # SHA1 hash
    sha1 = hashlib.sha1()
    # Encode secret
    sha1.update(str(secret).encode())
    # Get key
    key = sha1.digest()[:16]
    # Decrypt flag
    aes = AES.new(key, AES.MODE_CBC, iv)
    # Plain text
    plain = aes.decrypt(cipher)
    return plain

# Discrete logarithm calculator
def DLP(g, A, p):
    discrete_log(p, A, g)
    return discrete_log(p, A, g)

a = DLP(g, A, p)
print("Alice's secret key: ", a)
# Shared secret
secret = pow(B, a, p)
# Decrypt flag
flag=decrypt(secret, iv, encrypted_flag)
print("Flag: ", flag)
EOL
)

echo "$py_load" > "$py_file"
python3 "$py_file"
rm "$py_file"
rm out.txt
