#!/bin/bash

# Check if Digital Ocean already has SSH key, add it if necessary.
keys=`doctl compute ssh-key list`

if [[ $keys == *"$ssh_key_fingerprint"* ]]
then
    echo "SSH key already on Digital Ocean"
else
    echo "Adding the SSH Key to Digital Ocean"
    doctl compute ssh-key import $ssh_key_name --public-key-file $ssh_key_pub
fi
