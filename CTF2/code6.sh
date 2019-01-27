#!/bin/bash
while read IP; do 
    echo $IP >> kkk.txt
    curl  https://"$IP" -m 1 -k >> kkk.txt
done < IPs.txt
