#!/bin/dash

for i in "$@"; do
    display "$i"
    echo Address this email to? 
    read email

    echo Message to accompany image?
    read emailMessage
mutt -s "$emailMessage" -e 'set copy=no' -a "$i" -- "$email"

done