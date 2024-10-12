#!/usr/bin/env bash

read -s -p "Password: " password

openssl pkcs12 -in $1 -out wifi.crt -passin pass:$password -clcerts -nokeys
openssl pkcs12 -in $1 -out wifi.key -passin pass:$password -nocerts -nodes
