#!/bin/bash

num="11515195063862318899931685488813747395775516287289682636499965282714637259206269"
hex=$(python3 -c "print(hex($num)[2:])")
decoded_bytes=$(echo -n "$hex" | xxd -r -p)

echo "Decoded Bytes: $decoded_bytes"
