#!/bin/bash

for file in "$@"
do
    size="$(ls -l "$file" | awk '{print $5}')"
    dd if=/dev/urandom of="$file" bs="$size" count=1 2> /dev/null
    rm -f "$file"
done
