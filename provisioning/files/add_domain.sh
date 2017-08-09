#!/bin/bash

out=`doctl compute domain list | awk -v domain="$domain" '$1 == domain { print $0 }'`
if [ "$out" == "" ]
then
    doctl compute domain create "$domain" --ip-address "$ip"
fi