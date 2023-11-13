#!/bin/bash

archive_py="int.py"
openssl rsa -in transparency.pem -text -noout > key_info.txt
d_value=$(grep -A 18 "privateExponent:" key_info.txt | tr -d '\n' | tr -d "privateExponent:" |awk '{gsub(/[: ]/, "", $0); print}')
echo "Valor de d_value hex: $d_value"
echo "hex=\"$d_value\"" > "$archive.py"
echo "print(int(hex, 16))" >> "$archive.py"
int=$(python3 "$archive.py")
echo "Entero: $int"
rm "$archive.py"
rm key_info.txt
