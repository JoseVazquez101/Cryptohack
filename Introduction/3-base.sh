#!/bin/bash

#!/bin/bash

byte_string=$(echo -n "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" | xxd -r -p)
base64_encoded=$(echo -n "$byte_string" | base64)

echo "Encoded Base64: $base64_encoded"
